---
UID: NE.wdfio._WDF_IO_FORWARD_PROGRESS_ACTION
title: WDF_IO_FORWARD_PROGRESS_ACTION
author: windows-driver-content
description: The WDF_IO_FORWARD_PROGRESS_ACTION enumeration identifies actions that the framework can take for an I/O request packet (IRP) that your driver examines during a low-memory situation.
old-location: wdf\wdf_io_forward_progress_action.htm
old-project: wdf
ms.assetid: 4d63c908-8ae3-4df4-826f-9d87ea6c24ad
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_INTERRUPT_INFO, WDF_INTERRUPT_INFO, *PWDF_INTERRUPT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfio.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.9
req.umdf-ver: 
req.alt-api: WDF_IO_FORWARD_PROGRESS_ACTION
req.alt-loc: wdfio.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# WDF_IO_FORWARD_PROGRESS_ACTION enumeration



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_IO_FORWARD_PROGRESS_ACTION</b> enumeration identifies actions that the framework can take for an I/O request packet (IRP) that your driver examines during a low-memory situation.</p>


## -syntax

````
typedef enum _WDF_IO_FORWARD_PROGRESS_ACTION { 
  WdfIoForwardProgressActionInvalid             = 0x0,
  WdfIoForwardProgressActionFailRequest         = 0x1,
  WdfIoForwardProgressActionUseReservedRequest  = 0x2
} WDF_IO_FORWARD_PROGRESS_ACTION;
````


## -enum-fields
<dl>

### -field <a id="WdfIoForwardProgressActionInvalid"></a><a id="wdfioforwardprogressactioninvalid"></a><a id="WDFIOFORWARDPROGRESSACTIONINVALID"></a><b>WdfIoForwardProgressActionInvalid</b>

<dd>
<p>For internal use only.</p>
</dd>

### -field <a id="WdfIoForwardProgressActionFailRequest"></a><a id="wdfioforwardprogressactionfailrequest"></a><a id="WDFIOFORWARDPROGRESSACTIONFAILREQUEST"></a><b>WdfIoForwardProgressActionFailRequest</b>

<dd>
<p>The framework will complete the current I/O request with an error status value.</p>
</dd>

### -field <a id="WdfIoForwardProgressActionUseReservedRequest"></a><a id="wdfioforwardprogressactionusereservedrequest"></a><a id="WDFIOFORWARDPROGRESSACTIONUSERESERVEDREQUEST"></a><b>WdfIoForwardProgressActionUseReservedRequest</b>

<dd>
<p>The framework will use a reserved request object, if one is available, for the current I/O request.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_IO_FORWARD_PROGRESS_ACTION</b> enumeration is used as the return value for the <a href="..\wdfio\nc-wdfio-evt-wdf-io-wdm-irp-for-forward-progress.md">EvtIoWdmIrpForForwardProgress</a> callback function.</p>

<p>The <b>WDF_IO_FORWARD_PROGRESS_ACTION</b> enumeration is used as the return value for the <a href="..\wdfio\nc-wdfio-evt-wdf-io-wdm-irp-for-forward-progress.md">EvtIoWdmIrpForForwardProgress</a> callback function.</p>

<p>The <b>WDF_IO_FORWARD_PROGRESS_ACTION</b> enumeration is used as the return value for the <a href="..\wdfio\nc-wdfio-evt-wdf-io-wdm-irp-for-forward-progress.md">EvtIoWdmIrpForForwardProgress</a> callback function.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.9</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfio.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfio\nc-wdfio-evt-wdf-io-wdm-irp-for-forward-progress.md">EvtIoWdmIrpForForwardProgress</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_IO_FORWARD_PROGRESS_ACTION enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
