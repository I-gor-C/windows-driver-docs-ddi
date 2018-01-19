---
UID : NI:bthioctl.IOCTL_BTH_SDP_DISCONNECT
title : IOCTL_BTH_SDP_DISCONNECT
author : windows-driver-content
description : The IOCTL_BTH_SDP_DISCONNECT request closes a connection to a remote SDP server.
old-location : bltooth\ioctl_bth_sdp_disconnect.htm
old-project : bltooth
ms.assetid : 1d45465c-21ee-423c-967a-4462b61c2f0e
ms.author : windowsdriverdev
ms.date : 12/21/2017
ms.keywords : _HFP_BYPASS_CODEC_ID_V1, *PHFP_BYPASS_CODEC_ID_V1, HFP_BYPASS_CODEC_ID_V1
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : bthioctl.h
req.include-header : Bthioctl.h
req.target-type : Windows
req.target-min-winverclnt : Versions: Supported in Windows Vista, and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IOCTL_BTH_SDP_DISCONNECT
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

# IOCTL_BTH_SDP_DISCONNECT IOCTL
The IOCTL_BTH_SDP_DISCONNECT request closes a connection to a remote SDP server.



The IOCTL_BTH_SDP_DISCONNECT request closes a connection to a remote SDP server.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
The 
      <b>AssociatedIrp.SystemBuffer</b> member contains an 
      <a href="..\bthioctl\ns-bthioctl-_bth_sdp_disconnect.md">BTH_SDP_DISCONNECT</a> structure that
      specifies the connection handle to the remote SDP connection to terminate.

### Input Buffer Length
Length of an 
      <a href="..\bthioctl\ns-bthioctl-_bth_sdp_disconnect.md">BTH_SDP_DISCONNECT</a> structure.

### Output Buffer
None.

### Output Buffer Length
None.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
I/O Status block
The 
      <b>Information</b> member of the STATUS_BLOCK structure is set to zero.

The 
      <b>Status</b> member is set to one of the values in the following table.

STATUS_SUCCESS

The IOCTL completed successfully.

STATUS_DEVICE_NOT_CONNECTED

The specified SDP server has already been disconnected.

STATUS_INVALID_PARAMETER

The connection handle passed in the input buffer is invalid.

    ## Remarks
        Callers of 
    <a href="..\bthioctl\ni-bthioctl-ioctl_bth_sdp_connect.md">IOCTL_BTH_SDP_CONNECT</a> must issue an
    IOCTL_BTH_SDP_DISCONNECT IOCTL when the SDP connection is no longer needed. After
    IOCTL_BTH_SDP_DISCONNECT is called, the specified SDP handle is no longer valid.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | bthioctl.h (include Bthioctl.h) |
| **IRQL** | <= PASSIVE_LEVEL |

    ## See Also

        <dl>
<dt>
<a href="..\bthioctl\ns-bthioctl-_bth_sdp_disconnect.md">BTH_SDP_DISCONNECT</a>
</dt>
<dt>
<a href="..\bthioctl\ni-bthioctl-ioctl_bth_sdp_connect.md">IOCTL_BTH_SDP_CONNECT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20IOCTL_BTH_SDP_DISCONNECT control code%20 RELEASE:%20(12/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>