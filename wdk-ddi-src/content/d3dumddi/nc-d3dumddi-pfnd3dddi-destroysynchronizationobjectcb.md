---
UID: NC.d3dumddi.PFND3DDDI_DESTROYSYNCHRONIZATIONOBJECTCB
title: PFND3DDDI_DESTROYSYNCHRONIZATIONOBJECTCB
author: windows-driver-content
description: The pfnDestroySynchronizationObjectCb function destroys the synchronization object that was created through a call to the pfnCreateSynchronizationObjectCb function.
old-location: display\pfndestroysynchronizationobjectcb.htm
old-project: display
ms.assetid: 7ba549a2-f165-4b5e-8cf4-ab707222532c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnDestroySynchronizationObjectCb
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

# PFND3DDDI_DESTROYSYNCHRONIZATIONOBJECTCB callback



## -description
<p>The <b>pfnDestroySynchronizationObjectCb</b> function destroys the synchronization object that was created through a call to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createsynchronizationobjectcb.md">pfnCreateSynchronizationObjectCb</a> function.</p>


## -prototype

````
PFND3DDDI_DESTROYSYNCHRONIZATIONOBJECTCB pfnDestroySynchronizationObjectCb;

__checkReturn HRESULT APIENTRY CALLBACK pfnDestroySynchronizationObjectCb(
  _In_       HANDLE                                hDevice,
  _In_ const D3DDDICB_DESTROYSYNCHRONIZATIONOBJECT *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to a display device (that is, the graphics context).</p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544185">D3DDDICB_DESTROYSYNCHRONIZATIONOBJECT</a> structure that contains a handle to the synchronization object to destroy.</p>
</dd>
</dl>

## -returns
<p><b>pfnDestroySynchronizationObjectCb</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The synchronization object was successfully destroyed.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p>

<p> </p>

<p>This function might also return other HRESULT values.</p>

## -remarks


## -requirements
<table>
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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544185">D3DDDICB_DESTROYSYNCHRONIZATIONOBJECT</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createsynchronizationobjectcb.md">pfnCreateSynchronizationObjectCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_DESTROYSYNCHRONIZATIONOBJECTCB callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
