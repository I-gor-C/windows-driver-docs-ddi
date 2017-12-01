---
UID: NC.d3dumddi.PFND3DDDI_LOCK2CB
title: PFND3DDDI_LOCK2CB
author: windows-driver-content
description: The pfnLock2Cb function locks an allocation and obtains a pointer to the allocation from the display miniport driver or video memory manager.
old-location: display\pfnlock2cb.htm
old-project: display
ms.assetid: C046F34A-4304-4B96-8D7A-7A951016437F
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnLock2Cb
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
req.iface: 
---

# PFND3DDDI_LOCK2CB callback



## -description
<p>The <b>pfnLock2Cb</b> function locks an allocation and obtains a pointer to the allocation from the display miniport driver or video memory manager. </p>


## -prototype

````
PFND3DDDI_LOCK2CB pfnLock2Cb;

HRESULT APIENTRY CALLBACK* pfnLock2Cb(
  _In_    HANDLE         hDevice,
  _Inout_ D3DDDICB_LOCK2 *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to the display device (graphics context).</p>
</dd>

### -param <i>pData</i> [in, out]

<dd>
<p>A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddicb-lock2.md">D3DDDICB_LOCK2</a> structure that describes the allocation to lock.</p>
</dd>
</dl>

## -returns
<p>If this callback function succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

## -remarks
<p>With the Windows Display Driver Model (WDDM) v2 it is now the user mode driver's responsibility to handle the following tasks:</p>

<p>Synchronization of other lock types (not no-overwrite or discard)</p>

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
<a href="..\d3dumddi\ns-d3dumddi--d3dddicb-lock2.md">D3DDDICB_LOCK2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_LOCK2CB callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
