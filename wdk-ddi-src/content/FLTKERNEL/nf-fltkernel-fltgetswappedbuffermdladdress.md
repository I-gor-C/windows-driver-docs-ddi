---
UID: NF.fltkernel.FltGetSwappedBufferMdlAddress
title: FltGetSwappedBufferMdlAddress
author: windows-driver-content
description: The FltGetSwappedBufferMdlAddress routine returns the memory descriptor list (MDL) address for a buffer that was swapped in by a minifilter driver.
old-location: ifsk\fltgetswappedbuffermdladdress.htm
ms.assetid: 804263ec-8b3b-4a7c-9db4-ad524b807313
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltGetSwappedBufferMdlAddress
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: Any level
ms.keywords: FltGetSwappedBufferMdlAddress
req.iface: 
---

# FltGetSwappedBufferMdlAddress function



## -description
<p>The <b>FltGetSwappedBufferMdlAddress</b> routine returns the memory descriptor list (MDL) address for a buffer that was swapped in by a minifilter driver. </p>


## -syntax

````
PMDL FASTCALL FltGetSwappedBufferMdlAddress(
  _In_ PFLT_CALLBACK_DATA CallbackData
);
````


## -parameters
<dl>

### -param <i>CallbackData</i> [in]

<dd>
<p>Pointer to the callback data structure for the operation. </p>
</dd>
</dl>

## -returns
<p><b>FltGetSwappedBufferMdlAddress</b> returns the MDL address for the buffer that was swapped in by the caller. <b>FltGetSwappedBufferMdlAddress</b> returns <b>NULL</b> in the following cases: </p>

## -remarks
<p>A minifilter driver that swaps in a new buffer in a preoperation callback routine can get the MDL address for the buffer by calling <b>FltGetSwappedBufferMdlAddress</b> from the corresponding postoperation callback routine. </p>

<p>The <b>FltGetSwappedBufferMdlAddress</b> routine is necessary because the postoperation callback routine receives a callback data structure that contains the original buffer and MDL address, not the ones that were swapped in by the caller's preoperation callback routine. </p>

<p>It is possible for <b>FltGetSwappedBufferMdlAddress</b> to return a non-<b>NULL</b> MDL value even if the caller did not create an MDL for the buffer that it swapped in. This happens when an MDL is created for the buffer by a minifilter driver, legacy filter driver, or file system driver that is below the caller in the minifilter driver or file system driver stack. </p>

<p>It is also possible for <b>FltGetSwappedBufferMdlAddress</b> to return a non-<b>NULL</b> MDL value even if the caller did not swap in a new buffer in its preoperation callback routine. This happens in operations, such as paging I/O, where the buffer is <b>NULL</b>, and the caller swaps in a new MDL address. </p>

<p>The MDL for the buffer that was swapped in by the caller is automatically freed by the Filter Manager when the postoperation callback routine returns. To prevent this MDL from being freed, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544352">FltRetainSwappedBufferMdlAddress</a>. </p>

<p><b>FltGetSwappedBufferMdlAddress</b> can only be called from a postoperation callback routine. </p>

<p>A minifilter driver that swaps in a new buffer in a preoperation callback routine can get the MDL address for the buffer by calling <b>FltGetSwappedBufferMdlAddress</b> from the corresponding postoperation callback routine. </p>

<p>The <b>FltGetSwappedBufferMdlAddress</b> routine is necessary because the postoperation callback routine receives a callback data structure that contains the original buffer and MDL address, not the ones that were swapped in by the caller's preoperation callback routine. </p>

<p>It is possible for <b>FltGetSwappedBufferMdlAddress</b> to return a non-<b>NULL</b> MDL value even if the caller did not create an MDL for the buffer that it swapped in. This happens when an MDL is created for the buffer by a minifilter driver, legacy filter driver, or file system driver that is below the caller in the minifilter driver or file system driver stack. </p>

<p>It is also possible for <b>FltGetSwappedBufferMdlAddress</b> to return a non-<b>NULL</b> MDL value even if the caller did not swap in a new buffer in its preoperation callback routine. This happens in operations, such as paging I/O, where the buffer is <b>NULL</b>, and the caller swaps in a new MDL address. </p>

<p>The MDL for the buffer that was swapped in by the caller is automatically freed by the Filter Manager when the postoperation callback routine returns. To prevent this MDL from being freed, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544352">FltRetainSwappedBufferMdlAddress</a>. </p>

<p><b>FltGetSwappedBufferMdlAddress</b> can only be called from a postoperation callback routine. </p>

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
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541956">FltDecodeParameters</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544352">FltRetainSwappedBufferMdlAddress</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetSwappedBufferMdlAddress routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
