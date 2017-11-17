---
UID: NF.ks.KsMethodHandler
title: KsMethodHandler
author: windows-driver-content
description: The KsMethodHandler function handles methods requested through IOCTL_KS_METHOD. It works with all method identifiers defined by the sets. The function can only be called at PASSIVE_LEVEL.
old-location: stream\ksmethodhandler.htm
ms.assetid: 730b5fae-3536-44ed-8f92-e4563a137be9
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsMethodHandler
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
ms.keywords: KsMethodHandler
req.iface: 
---

# KsMethodHandler function



## -description
<p>The <b>KsMethodHandler</b> function handles methods requested through IOCTL_KS_METHOD. It works with all method identifiers defined by the sets. The function can only be called at PASSIVE_LEVEL.</p>


## -syntax

````
NTSTATUS KsMethodHandler(
  _In_       PIRP         Irp,
  _In_       ULONG        MethodSetsCount,
  _In_ const KSMETHOD_SET *MethodSet
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>Specifies the IRP with the method request being handled.</p>
</dd>

### -param <i>MethodSetsCount</i> [in]

<dd>
<p>Indicates the number of method set structures being passed.</p>
</dd>

### -param <i>MethodSet</i> [in]

<dd>
<p>Specifies the pointer to the list of method set information.</p>
</dd>
</dl>

## -returns
<p>The <b>KsMethodHandler</b> function returns STATUS_SUCCESS if successful, or an error specific to the method being handled if unsuccessful. The function always sets the IO_STATUS_BLOCK.Information field of the PIRP.IoStatus element within the IRP to zero because of an internal error, unless the element is set by a method handler. The function does not set the IO_STATUS_BLOCK.Status field nor complete the IRP.</p>

## -remarks
<p>The owner of a method set can perform prefiltering or postfiltering of the method handling using the <b>KsMethodHandler</b> and <b>KsFastMethodHandler </b>functions.</p>

<p>The owner of a method set can perform prefiltering or postfiltering of the method handling using the <b>KsMethodHandler</b> and <b>KsFastMethodHandler </b>functions.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561940">KsFastMethodHandler</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563401">KsMethodHandlerWithAllocator</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsMethodHandler function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
