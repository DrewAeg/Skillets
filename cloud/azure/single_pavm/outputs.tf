output "pavm_public_ip" {
    value = "${azurerm_public_ip.pavm_public_ip.ip_address}"
}

