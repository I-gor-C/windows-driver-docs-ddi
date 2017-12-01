---
UID: NS.wdfrequest._WDF_REQUEST_REUSE_PARAMS
title: WDF_REQUEST_REUSE_PARAMS
author: windows-driver-content
description: The WDF_REQUEST_REUSE_PARAMS structure specifies information that is associated with a reused I/O request.
old-location: wdf\wdf_request_reuse_params.htm
old-project: wdf
ms.assetid: 292e8a75-2035-4333-8a3c-28e79549d374
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_REQUEST_REUSE_PARAMS, WDF_REQUEST_REUSE_PARAMS, *PWDF_REQUEST_REUSE_PARAMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_REQUEST_REUSE_PARAMS
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WDF_REQUEST_REUSE_PARAMS structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_REQUEST_REUSE_PARAMS</b> structure specifies information that is associated with a reused I/O request.</p>


## -syntax

````
typedef struct _WDF_REQUEST_REUSE_PARAMS {
  ULONG    Size;
  ULONG    Flags;
  NTSTATUS Status;
  PIRP     NewIrp;
} WDF_REQUEST_REUSE_PARAMS, *PWDF_REQUEST_REUSE_PARAMS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bitwise OR of one or more <a href="..\wdfrequest\ne-wdfrequest--wdf-request-reuse-flags.md">WDF_REQUEST_REUSE_FLAGS</a>-typed flags.</p>
</dd>

### -field <b>Status</b>

<dd>
<p>An NTSTATUS value that the framework assigns to the request.</p>
</dd>

### -field <b>NewIrp</b>

<dd>
<p>A pointer to an <a href="..\ntifs\ns-ntifs--irp.md">IRP</a> structure. This member's value is optional and can be <b>NULL</b>. </p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_REQUEST_REUSE_PARAMS</b> structure is used as input to <a href="..\wdfrequest\nf-wdfrequest-wdfrequestreuse.md">WdfRequestReuse</a>.</p>

<p>To initialize this structure, the driver must call <a href="..\wdfrequest\nf-wdfrequest-wdf-request-reuse-params-init.md">WDF_REQUEST_REUSE_PARAMS_INIT</a>. To set a <b>NewIrp</b> value in the structure, the driver must call <a href="..\wdfrequest\nf-wdfrequest-wdf-request-reuse-params-set-new-irp.md">WDF_REQUEST_REUSE_PARAMS_SET_NEW_IRP</a> after calling <b>WDF_REQUEST_REUSE_PARAMS_INIT</b>.</p>

<p>If a lower driver needs to access the <b>Status</b> value, it can find it in the <b>Irp-&gt;IoStatus.Status</b> field.</p>

<p>You can set a <b>NewIrp</b> value only if the I/O request that you supply to <a href="..\wdfrequest\nf-wdfrequest-wdfrequestreuse.md">WdfRequestReuse</a> was created by calling <a href="..\wdfrequest\nf-wdfrequest-wdfrequestcreate.md">WdfRequestCreate</a> or <a href="..\wdfrequest\nf-wdfrequest-wdfrequestcreatefromirp.md">WdfRequestCreateFromIrp</a>.</p>

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
<a href="..\wdfrequest\nf-wdfrequest-wdfrequestcreatefromirp.md">WdfRequestCreateFromIrp</a>
</dt>
<dt>
<a href="..\wdfrequest\nf-wdfrequest-wdfrequestreuse.md">WdfRequestReuse</a>
</dt>
<dt>
<a href="..\wdfrequest\nf-wdfrequest-wdf-request-reuse-params-init.md">WDF_REQUEST_REUSE_PARAMS_INIT</a>
</dt>
<dt>
<a href="..\wdfrequest\nf-wdfrequest-wdf-request-reuse-params-set-new-irp.md">WDF_REQUEST_REUSE_PARAMS_SET_NEW_IRP</a>
</dt>
<dt>
<a href="..\wdfrequest\ne-wdfrequest--wdf-request-reuse-flags.md">WDF_REQUEST_REUSE_FLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_REQUEST_REUSE_PARAMS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
