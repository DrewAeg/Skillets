output "pavm_public_ip_address" {
    value = "${azurerm_public_ip.pavm_public_ip.ip_address}"
}

