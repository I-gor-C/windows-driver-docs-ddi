---
UID: NC.d3dumddi.PFND3DDDI_DEALLOCATE2CB
title: PFND3DDDI_DEALLOCATE2CB
author: windows-driver-content
description: The pfnDeallocate2Cb user mode callback function releases allocations for a kernel-mode resource object if the resource object was created.
old-location: display\pfndeallocate2cb.htm
ms.assetid: 68C7EC44-D744-4C69-86D9-35B3B089875A
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnDeallocate2Cb
req.alt-loc: d3dumddi.h
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
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
req.iface: 
---

# PFND3DDDI_DEALLOCATE2CB callback



## -description
<p>The <b>pfnDeallocate2Cb</b> user mode callback function releases allocations for a kernel-mode resource object if the resource object was created.</p>
<p><b>pfnDeallocate2Cb</b> is a replacement for <a href="https://msdn.microsoft.com/2ffa0367-0451-45d2-be05-e450c45be116">pfnDeallocateCb</a> that has an additional <b>Flags</b> member. When <b>Flags</b> are set to all zeroes, behavior is equivalent to <i>pfnDeallocateCb</i>.
  </p>


## -prototype

````
PFND3DDDI_DEALLOCATE2CB pfnDeallocate2Cb;

_Check_return_ HRESULT APIENTRY CALLBACK* pfnDeallocate2Cb(
  _In_       HANDLE               hDevice,
  _In_ const D3DDDICB_DEALLOCATE2 *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to the display device (graphics context).</p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn906761">D3DDDICB_DEALLOCATE2</a> structure that describes the resource to release.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The memory was successfully released.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p>

<p> </p>

<p>This function might also return other HRESULT values.</p>

## -remarks
<p>When an allocation destruction request is received, VidMm assumes, by default, that commands queued prior to the destruction request may access the allocation being destroyed and defers the destruction operation until the queued commands finish. If the user mode driver (UMD) knows that pending commands don’t access the allocation being destroyed, it can instruct VidMm not to wait until pending commands are finished by setting the <b>AssumeNotInUse</b> flag to <b>TRUE</b> when calling <b>pfnDeallocate2Cb</b>.</p>

<p>If an application or UMD would like to ensure allocation memory is reclaimed prior to the return from the <b>pfnDeallocate2Cb</b> call (for example, to minimize peak memory usage if the surface is being re-created), it should set the <b>SynchronousDestroy</b> flag.
</p>

<p>When an allocation destruction request is received, VidMm assumes, by default, that commands queued prior to the destruction request may access the allocation being destroyed and defers the destruction operation until the queued commands finish. If the user mode driver (UMD) knows that pending commands don’t access the allocation being destroyed, it can instruct VidMm not to wait until pending commands are finished by setting the <b>AssumeNotInUse</b> flag to <b>TRUE</b> when calling <b>pfnDeallocate2Cb</b>.</p>

<p>If an application or UMD would like to ensure allocation memory is reclaimed prior to the return from the <b>pfnDeallocate2Cb</b> call (for example, to minimize peak memory usage if the surface is being re-created), it should set the <b>SynchronousDestroy</b> flag.
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906761">D3DDDICB_DEALLOCATE2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/2ffa0367-0451-45d2-be05-e450c45be116">pfnDeallocateCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_DEALLOCATE2CB callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
