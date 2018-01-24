---
UID : NI:bthioctl.IOCTL_BTH_GET_LOCAL_INFO
title : IOCTL_BTH_GET_LOCAL_INFO
author : windows-driver-content
description : The IOCTL_BTH_GET_LOCAL_INFO request returns information about the local Bluetooth system and radio.
old-location : bltooth\ioctl_bth_get_local_info.htm
old-project : bltooth
ms.assetid : 0eaee91f-c3d1-4715-9d7a-15dc3935eb36
ms.author : windowsdriverdev
ms.date : 12/21/2017
ms.keywords : _HFP_BYPASS_CODEC_ID_V1, *PHFP_BYPASS_CODEC_ID_V1, HFP_BYPASS_CODEC_ID_V1
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : bthioctl.h
req.include-header : Bthioctl.h
req.target-type : Windows
req.target-min-winverclnt : Supported in Windows Vista, and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IOCTL_BTH_GET_LOCAL_INFO
req.alt-loc : Bthioctl.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : <= PASSIVE_LEVEL
req.typenames : "*PHFP_BYPASS_CODEC_ID_V1, HFP_BYPASS_CODEC_ID_V1"
---

# IOCTL_BTH_GET_LOCAL_INFO IOCTL
The IOCTL_BTH_GET_LOCAL_INFO request returns information about the local Bluetooth system and
     radio.



The IOCTL_BTH_GET_LOCAL_INFO request returns information about the local Bluetooth system and
     radio.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
The 
      <b>AssociatedIrp.SystemBuffer</b> member points to a buffer for a 
      <a href="..\bthioctl\ns-bthioctl-_bth_local_radio_info.md">BTH_LOCAL_RADIO_INFO</a> structure.

### Input Buffer Length
The length of a 
      <a href="..\bthioctl\ns-bthioctl-_bth_local_radio_info.md">BTH_LOCAL_RADIO_INFO</a> structure.

### Output Buffer
The 
      <b>AssociatedIrp.SystemBuffer</b> member points to a buffer that holds a 
      <a href="..\bthioctl\ns-bthioctl-_bth_local_radio_info.md">BTH_LOCAL_RADIO_INFO</a> structure. The
      buffer contains information about the local radio, including a 
      <a href="http://go.microsoft.com/fwlink/p/?linkid=50713">BTH_DEVICE_INFO</a> structure and a 
      <a href="..\bthioctl\ns-bthioctl-_bth_radio_info.md">BTH_RADIO_INFO</a> structure.

### Output Buffer Length
The length of a 
      <a href="..\bthioctl\ns-bthioctl-_bth_local_radio_info.md">BTH_LOCAL_RADIO_INFO</a> structure.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
I/O Status block
The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to the size, in bytes, of the output
      buffer.

The 
      <b>Status</b> member of the STATUS_BLOCK structure is always set to STATUS_SUCCESS.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | bthioctl.h (include Bthioctl.h) |
| **IRQL** | <= PASSIVE_LEVEL |

    ## See Also

        <dl>
<dt>
<a href="..\bthioctl\ns-bthioctl-_bth_local_radio_info.md">BTH_LOCAL_RADIO_INFO</a>
</dt>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=50713">BTH_DEVICE_INFO</a></dt>
<dt>
<a href="..\bthioctl\ns-bthioctl-_bth_radio_info.md">BTH_RADIO_INFO</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20IOCTL_BTH_GET_LOCAL_INFO control code%20 RELEASE:%20(12/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>