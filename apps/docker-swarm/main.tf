provider "proxmox" {
  endpoint  = var.pm_api_url
  api_token = "${var.pm_api_token_id}=${var.pm_api_token_secret}"
  insecure  = var.pm_tls_insecure
}

locals {
  manager_ip = "${var.lxc_ip_base}.10"
  worker_ips = ["${var.lxc_ip_base}.11", "${var.lxc_ip_base}.12"]
}

resource "proxmox_virtual_environment_container" "manager" {
  node_name = var.target_node
  vm_id     = var.manager_id

  unprivileged = true
  started      = true

  features {
    nesting = true
  }

  cpu {
    cores = 2
  }

  memory {
    dedicated = 2048
  }

  disk {
    datastore_id = var.lxc_storage
    size         = 8
  }

  network_interface {
    name   = "veth0"
    bridge = "vmbr0"
  }

  initialization {
    hostname = "swarm-manager-1"

    ip_config {
      ipv4 {
        address = "${local.manager_ip}/${var.lxc_netmask}"
        gateway = var.lxc_gateway
      }
    }

    user_account {
      password = var.lxc_root_password
      keys     = [var.lxc_ssh_public_key]
    }
  }

  operating_system {
    template_file_id = var.lxc_template
    type             = "ubuntu"
  }
}

resource "proxmox_virtual_environment_container" "workers" {
  count     = 2
  node_name = var.target_node
  vm_id     = var.worker_ids[count.index]

  unprivileged = true
  started      = true

  features {
    nesting = true
  }

  cpu {
    cores = 2
  }

  memory {
    dedicated = 2048
  }

  disk {
    datastore_id = var.lxc_storage
    size         = 8
  }

  network_interface {
    name   = "veth0"
    bridge = "vmbr0"
  }

  initialization {
    hostname = "swarm-worker-${count.index + 1}"

    ip_config {
      ipv4 {
        address = "${local.worker_ips[count.index]}/${var.lxc_netmask}"
        gateway = var.lxc_gateway
      }
    }

    user_account {
      password = var.lxc_root_password
      keys     = [var.lxc_ssh_public_key]
    }
  }

  operating_system {
    template_file_id = var.lxc_template
    type             = "ubuntu"
  }
}

resource "null_resource" "install_docker_manager" {
  depends_on = [proxmox_virtual_environment_container.manager]

  connection {
    type     = "ssh"
    user     = "root"
    password = var.lxc_root_password
    host     = local.manager_ip
  }

  provisioner "remote-exec" {
    inline = [
      "apt-get update -y",
      "apt-get install -y ${var.docker_package}",
      "systemctl enable --now docker",
      "docker swarm init --advertise-addr ${var.swarm_advertise_addr} || true"
    ]
  }
}

resource "null_resource" "install_docker_workers" {
  count      = 2
  depends_on = [proxmox_virtual_environment_container.workers]

  connection {
    type     = "ssh"
    user     = "root"
    password = var.lxc_root_password
    host     = local.worker_ips[count.index]
  }

  provisioner "remote-exec" {
    inline = [
      "apt-get update -y",
      "apt-get install -y ${var.docker_package}",
      "systemctl enable --now docker"
    ]
  }
}

resource "null_resource" "swarm_join" {
  depends_on = [null_resource.install_docker_manager, null_resource.install_docker_workers]

  provisioner "local-exec" {
    command = <<EOT
set -e
TOKEN=$(ssh -o StrictHostKeyChecking=no root@${local.manager_ip} docker swarm join-token -q worker)
ssh -o StrictHostKeyChecking=no root@${local.worker_ips[0]} docker swarm join --token $TOKEN ${local.manager_ip}:2377 || true
ssh -o StrictHostKeyChecking=no root@${local.worker_ips[1]} docker swarm join --token $TOKEN ${local.manager_ip}:2377 || true
EOT
  }
}

resource "null_resource" "portainer" {
  depends_on = [null_resource.swarm_join]

  connection {
    type     = "ssh"
    user     = "root"
    password = var.lxc_root_password
    host     = local.manager_ip
  }

  provisioner "remote-exec" {
    inline = [
      "docker network inspect portainer_agent_network >/dev/null 2>&1 || docker network create -d overlay portainer_agent_network",
      "docker service ls --format '{{.Name}}' | grep -q '^portainer_agent$' || docker service create --name portainer_agent --network portainer_agent_network --mode global --constraint 'node.platform.os == linux' --mount type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock --mount type=bind,src=/var/lib/docker/volumes,dst=/var/lib/docker/volumes portainer/agent:${var.portainer_version}",
      "docker service ls --format '{{.Name}}' | grep -q '^portainer$' || docker service create --name portainer --publish ${var.portainer_http_port}:9000 --publish ${var.portainer_https_port}:9443 --constraint 'node.role == manager' --network portainer_agent_network --replicas 1 --mount type=volume,src=portainer_data,dst=/data portainer/portainer-ce:${var.portainer_version} --tlsskipverify"
    ]
  }
}
