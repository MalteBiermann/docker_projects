output "manager_ip" {
  value       = "${var.lxc_ip_base}.10"
  description = "Swarm manager IP"
}

output "worker_ips" {
  value       = ["${var.lxc_ip_base}.11", "${var.lxc_ip_base}.12"]
  description = "Swarm worker IPs"
}
