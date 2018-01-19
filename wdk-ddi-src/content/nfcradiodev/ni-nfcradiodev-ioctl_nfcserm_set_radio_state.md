---
UID : NI:nfcradiodev.IOCTL_NFCSERM_SET_RADIO_STATE
title : IOCTL_NFCSERM_SET_RADIO_STATE
author : windows-driver-content
description : This IOCTL is used by the SE radio management application or service to query the current radio power state of the proximity device.
old-location : nfpdrivers\ioctl_nfcserm_set_radio_state.htm
old-project : nfpdrivers
ms.assetid : 721AE7FE-927C-4EBA-B33D-C5A5A986951C
ms.author : windowsdriverdev
ms.date : 12/18/2017
ms.keywords : _NFC_CX_RF_DISCOVERY_CONFIG, NFC_CX_RF_DISCOVERY_CONFIG, *PNFC_CX_RF_DISCOVERY_CONFIG
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : nfcradiodev.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IOCTL_NFCSERM_SET_RADIO_STATE
req.alt-loc : nfcradiodev.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : NFC_CX_RF_DISCOVERY_CONFIG, *PNFC_CX_RF_DISCOVERY_CONFIG
---

# IOCTL_NFCSERM_SET_RADIO_STATE IOCTL
This IOCTL is used by the SE radio management application or service to query the current radio power state of the proximity device.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
<a href="..\nfcradiodev\ns-nfcradiodev-_nfcrm_set_radio_state.md"> NFCRM_SET_RADIO_STATE structure</a>

### Input Buffer Length
sizeof(NFCRM_SET_RADIO_STATE)

### Output Buffer
None

### Output Buffer Length
None

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
I/O Status block
<b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | nfcradiodev.h |
| **IRQL** |  |