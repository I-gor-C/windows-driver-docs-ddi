---
UID: NE.wdfrequest._WDF_REQUEST_REUSE_FLAGS
title: WDF_REQUEST_REUSE_FLAGS
author: windows-driver-content
description: The WDF_REQUEST_REUSE_FLAGS enumeration type defines flags that are used in a driver's WDF_REQUEST_REUSE_PARAMS structure.
old-location: wdf\wdf_request_reuse_flags.htm
old-project: wdf
ms.assetid: 3d1f8f38-b875-4661-9941-4dec28b7e8fb
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfRegistryWdmGetHandle
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_REQUEST_REUSE_FLAGS
req.alt-loc: wdfrequest.h
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
req.iface: 
req.product: Windows 10 or later.
---

# WDF_REQUEST_REUSE_FLAGS enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_REQUEST_REUSE_FLAGS</b> enumeration type defines flags that are used in a driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552480">WDF_REQUEST_REUSE_PARAMS</a> structure.</p>


## -syntax

````
typedef enum _WDF_REQUEST_REUSE_FLAGS { 
  WDF_REQUEST_REUSE_NO_FLAGS     = 0x00000000,
  WDF_REQUEST_REUSE_SET_NEW_IRP  = 0x00000001
} WDF_REQUEST_REUSE_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="WDF_REQUEST_REUSE_NO_FLAGS"></a><a id="wdf_request_reuse_no_flags"></a><b>WDF_REQUEST_REUSE_NO_FLAGS</b>

<dd>
<p>No flags are set.</p>
</dd>

### -field <a id="WDF_REQUEST_REUSE_SET_NEW_IRP"></a><a id="wdf_request_reuse_set_new_irp"></a><b>WDF_REQUEST_REUSE_SET_NEW_IRP</b>

<dd>
<p>The <b>NewIrp</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552480">WDF_REQUEST_REUSE_PARAMS</a> structure is valid.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfrequest.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552480">WDF_REQUEST_REUSE_PARAMS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_REQUEST_REUSE_FLAGS enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
