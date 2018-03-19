---
UID: NI:bthhfpddi.IOCTL_BTHHFP_DEVICE_GET_CONTAINERID
title: IOCTL_BTHHFP_DEVICE_GET_CONTAINERID
author: windows-driver-content
description: The IOCTL_BTHHFP_DEVICE_GET_CONTAINERID IOCTL Gets the PnP Container ID of the Bluetooth device.
old-location: audio\ioctl_bthhfp_device_get_containerid.htm
old-project: audio
ms.assetid: 23B6CB2C-8290-42D7-AA68-6D335ED1818A
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: IOCTL_BTHHFP_DEVICE_GET_CONTAINERID, IOCTL_BTHHFP_DEVICE_GET_CONTAINERID control code [Audio Devices], audio.ioctl_bthhfp_device_get_containerid, bthhfpddi/IOCTL_BTHHFP_DEVICE_GET_CONTAINERID
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: bthhfpddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Bthhfpddi.h
api_name:
-	IOCTL_BTHHFP_DEVICE_GET_CONTAINERID
product: Windows
targetos: Windows
req.typenames: HFP_BYPASS_CODEC_ID_VERSION, *PHFP_BYPASS_CODEC_ID_VERSION
---

# IOCTL_BTHHFP_DEVICE_GET_CONTAINERID IOCTL
The <b>IOCTL_BTHHFP_DEVICE_GET_CONTAINERID</b> 
   IOCTL Gets the PnP Container ID of the Bluetooth device.
<div class="alert"><b>Note</b>  This IOCTL has been deprecated for Windows 8.1, so you should use <a href="..\bthhfpddi\ni-bthhfpddi-ioctl_bthhfp_device_get_descriptor.md">IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR</a> instead.</div><div> </div>

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
None.

### Input Buffer Length
None.

### Output Buffer
A GUID that is the Container ID.

### Output Buffer Length
The size of a GUID.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
N/A

## Remarks
This request completes immediately.

The audio driver stores this container ID in appropriate context data and returns it in the driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265129">KSPROPERTY_JACK_CONTAINERID</a> KS property.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | bthhfpddi.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn302027">Bluetooth HFP DDI IOCTLs</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn265129">KSPROPERTY_JACK_CONTAINERID</a>



<a href="..\bthhfpddi\ni-bthhfpddi-ioctl_bthhfp_device_get_descriptor.md">IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR</a>