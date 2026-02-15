variable "pm_api_url" {
  type        = string
  description = "Proxmox API endpoint (e.g., https://proxmox.local:8006/)"
}

variable "pm_api_token_id" {
  type        = string
  description = "Proxmox API token ID (user@pve!token)"
  sensitive   = true
}

variable "pm_api_token_secret" {
  type        = string
  description = "Proxmox API token secret"
  sensitive   = true
}

variable "pm_tls_insecure" {
  type        = bool
  description = "Allow insecure TLS"
  default     = true
}

variable "target_node" {
  type        = string
  description = "Proxmox node name to place the LXC containers on"
}

variable "lxc_template" {
  type        = string
  description = "LXC template (e.g., local:vztmpl/ubuntu-22.04-standard_22.04-1_amd64.tar.zst)"
}

variable "lxc_storage" {
  type        = string
  description = "Storage name for rootfs (e.g., local-lvm)"
}

variable "lxc_gateway" {
  type        = string
  description = "Default gateway for LXC containers"
}

variable "lxc_netmask" {
  type        = string
  description = "Netmask in CIDR or dotted form (e.g., 24 or 255.255.255.0)"
}

variable "lxc_ip_base" {
  type        = string
  description = "Base IP (first three octets) for LXC IPs, e.g., 192.168.1"
}

variable "lxc_ssh_public_key" {
  type        = string
  description = "SSH public key for root access"
}

variable "lxc_root_password" {
  type        = string
  description = "Root password for LXC containers"
  sensitive   = true
}

variable "manager_id" {
  type        = number
  description = "VMID for swarm manager"
  default     = 200
}

variable "worker_ids" {
  type        = list(number)
  description = "VMIDs for swarm workers"
  default     = [201, 202]
}

variable "swarm_advertise_addr" {
  type        = string
  description = "Swarm advertise address (usually the manager IP)"
}

variable "docker_package" {
  type        = string
  description = "Docker engine package name"
  default     = "docker.io"
}

variable "portainer_version" {
  type        = string
  description = "Portainer CE image version"
  default     = "2.20.3"
}

variable "portainer_http_port" {
  type        = number
  description = "Portainer HTTP port"
  default     = 9000
}

variable "portainer_https_port" {
  type        = number
  description = "Portainer HTTPS port"
  default     = 9443
}
