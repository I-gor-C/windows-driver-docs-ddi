---
UID: NC.d3dumddi.PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECT2CB
title: PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECT2CB
author: windows-driver-content
description: Inserts a signal on the specified synchronization objects in the specified context direct memory access (DMA) stream. Used by WDDM 1.2 and later user-mode display drivers.
old-location: display\pfnsignalsynchronizationobject2cb.htm
old-project: display
ms.assetid: 01B5E793-D075-42B5-9ADF-D033249AEE9F
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnSignalSynchronizationObject2Cb
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

# PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECT2CB callback



## -description
<p>Inserts a signal on the specified synchronization objects in the specified context direct memory access (DMA) stream. Used by WDDM 1.2 and later user-mode display drivers.</p>


## -prototype

````
PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECT2CB pfnSignalSynchronizationObject2Cb;

__checkResult HRESULT APIENTRY CALLBACK* pfnSignalSynchronizationObject2Cb(
  _In_       HANDLE                                hDevice,
  _In_ const D3DDDICB_SIGNALSYNCHRONIZATIONOBJECT2 *pData
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
<p>A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddicb-signalsynchronizationobject2.md">D3DDDICB_SIGNALSYNCHRONIZATIONOBJECT2</a> structure that describes the synchronization objects and context DMA stream that signaling is set up on. </p>
</dd>
</dl>

## -returns
<p>
      Returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The signaling was successfully set up.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p>

<p> </p>

<p>This function might also return other HRESULT values.</p>

## -remarks
<p>The <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createsynchronizationobject2cb.md">pfnCreateSynchronizationObject2Cb</a> function returns a kernel-mode handle to the newly created synchronization object in the <b>hSyncObject</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddicb-createsynchronizationobject2.md">D3DDDICB_CREATESYNCHRONIZATIONOBJECT2</a> structure that the <i>pData</i> parameter points to. The user-mode display driver passes this handle in calls to the following functions:</p>

<p>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroysynchronizationobjectcb.md">pfnDestroySynchronizationObjectCb</a>
</p>

<p><i>pfnSignalSynchronizationObject2Cb</i></p>

<p>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-waitforsynchronizationobject2cb.md">pfnWaitForSynchronizationObject2Cb</a>
</p>

<p>The <i>pfnSignalSynchronizationObject2Cb</i> function submits a signal command to the command stream of all Microsoft Direct3D contexts that are specified by the <b>hContext</b> and <b>BroadcastContext</b> members of the  <a href="..\d3dumddi\ns-d3dumddi--d3dddicb-signalsynchronizationobject2.md">D3DDDICB_SIGNALSYNCHRONIZATIONOBJECT2</a> structure. The synchronization objects are signaled only when all submitted signal commands are processed.</p>

<p>If synchronization objects are of type <b>D3DDDI_FENCE</b> (where <a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-synchronizationobjectinfo2.md">D3DDDI_SYNCHRONIZATIONOBJECTINFO2</a>.<b>Type</b> = <b>D3DDDI_FENCE</b>), they must be submitted only one at a time, and <a href="..\d3dumddi\ns-d3dumddi--d3dddicb-signalsynchronizationobject2.md">D3DDDICB_SIGNALSYNCHRONIZATIONOBJECT2</a>.<i>ObjectCount</i> must have a value of 1.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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
<a href="..\d3dumddi\ns-d3dumddi--d3dddicb-createsynchronizationobject2.md">D3DDDICB_CREATESYNCHRONIZATIONOBJECT2</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddicb-signalsynchronizationobject2.md">D3DDDICB_SIGNALSYNCHRONIZATIONOBJECT2</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createsynchronizationobject2cb.md">pfnCreateSynchronizationObject2Cb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroysynchronizationobjectcb.md">pfnDestroySynchronizationObjectCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-waitforsynchronizationobject2cb.md">pfnWaitForSynchronizationObject2Cb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECT2CB callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
