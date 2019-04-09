output "pavm_public_ip_address" {
    value = "${azurerm_public_ip.pavm_public_ip.ip_address}"
}

output "pavm_resource_group" {
    value = "${azurerm_resource_group.panhandler.name}"
}
