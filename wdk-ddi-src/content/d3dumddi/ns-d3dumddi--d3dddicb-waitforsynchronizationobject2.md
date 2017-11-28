---
UID: NS.d3dumddi._D3DDDICB_WAITFORSYNCHRONIZATIONOBJECT2
title: D3DDDICB_WAITFORSYNCHRONIZATIONOBJECT2
author: windows-driver-content
description: Describes the parameters that are required to set up the wait in a call to the pfnWaitForSynchronizationObject2Cb function.
old-location: display\d3dddicb_waitforsynchronizationobject2.htm
old-project: display
ms.assetid: b5dbd1f3-4475-41d2-879a-34618b28b485
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDICB_WAITFORSYNCHRONIZATIONOBJECT2, D3DDDICB_WAITFORSYNCHRONIZATIONOBJECT2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDICB_WAITFORSYNCHRONIZATIONOBJECT2
req.alt-loc: D3dumddi.h
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

# D3DDDICB_WAITFORSYNCHRONIZATIONOBJECT2 structure



## -description
<p>Describes the parameters that are required to set up the wait in a call to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-waitforsynchronizationobject2cb.md">pfnWaitForSynchronizationObject2Cb</a> function.</p>


## -syntax

````
typedef struct _D3DDDICB_WAITFORSYNCHRONIZATIONOBJECT2 {
  HANDLE        hContext;
  UINT          ObjectCount;
  D3DKMT_HANDLE ObjectHandleArray[D3DDDI_MAX_OBJECT_WAITED_ON];
  UINT64        FenceValue;
} D3DDDICB_WAITFORSYNCHRONIZATIONOBJECT2;
````


## -struct-fields
<dl>

### -field <b>hContext</b>

<dd>
<p>[in] A handle to a Direct3D context that waits for the synchronization objects in the array that the <b>ObjectHandleArray</b> member specifies to occur.</p>
</dd>

### -field <b>ObjectCount</b>

<dd>
<p>[in] The number of synchronization objects in the <b>ObjectHandleArray</b> array.</p>
<p><b>ObjectHandleArray</b> must be set to 1 if the GPU synchronization object is of type <b>D3DDDI_FENCE</b>—namely, the <b>Type</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544658">D3DDDI_SYNCHRONIZATIONOBJECTINFO2</a> structure has a value of <b>D3DDDI_FENCE</b>.</p>
</dd>

### -field <b>ObjectHandleArray</b>

<dd>
<p>[in] An array of handles to the GPU synchronization objects that are to be signaled. The <b>D3DDDI_MAX_OBJECT_WAITED_ON</b> constant, which is defined as 32, indicates the maximum number of synchronization objects that the context can wait for.</p>
<p>All synchronization objects must be created on a logical adapter that has its context specified by the <b>hContext</b> member.</p>
</dd>

### -field <b>FenceValue</b>

<dd>
<p>[in] A 64-bit value that specifies the current fence value of the GPU synchronization object that is to be waited on.</p>
<p>This value applies only if the GPU synchronization object is of type <b>D3DDDI_FENCE</b>—namely, the <b>Type</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544658">D3DDDI_SYNCHRONIZATIONOBJECTINFO2</a> structure has a value of <b>D3DDDI_FENCE</b>.</p>
</dd>
</dl>

## -remarks
<p>Synchronization objects of type <b>D3DDDI_CPU_NOTIFICATION</b> cannot be used to wait on calls to <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-waitforsynchronizationobject2cb.md">pfnWaitForSynchronizationObject2Cb</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544658">D3DDDI_SYNCHRONIZATIONOBJECTINFO2</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-waitforsynchronizationobject2cb.md">pfnWaitForSynchronizationObject2Cb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_WAITFORSYNCHRONIZATIONOBJECT2 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
