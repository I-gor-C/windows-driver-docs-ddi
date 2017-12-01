---
UID: NS.d3dkmthk._D3DKMT_CREATECONTEXT
title: D3DKMT_CREATECONTEXT
author: windows-driver-content
description: The D3DKMT_CREATECONTEXT structure describes a kernel-mode device context to create.
old-location: display\d3dkmt_createcontext.htm
old-project: display
ms.assetid: 867705b9-a721-48a6-b1bc-6a75d5a03a21
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_CREATECONTEXT, D3DKMT_CREATECONTEXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_CREATECONTEXT
req.alt-loc: d3dkmthk.h
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

# D3DKMT_CREATECONTEXT structure



## -description
<p>The D3DKMT_CREATECONTEXT structure describes a kernel-mode device context to create.</p>


## -syntax

````
typedef struct _D3DKMT_CREATECONTEXT {
  D3DKMT_HANDLE             hDevice;
  UINT                      NodeOrdinal;
  UINT                      EngineAffinity;
  D3DDDI_CREATECONTEXTFLAGS Flags;
  VOID                      *pPrivateDriverData;
  UINT                      PrivateDriverDataSize;
  D3DKMT_CLIENTHINT         ClientHint;
  D3DKMT_HANDLE             hContext;
  VOID                      *pCommandBuffer;
  UINT                      CommandBufferSize;
  D3DDDI_ALLOCATIONLIST     *pAllocationList;
  UINT                      AllocationListSize;
  D3DDDI_PATCHLOCATIONLIST  *pPatchLocationList;
  UINT                      PatchLocationListSize;
  D3DGPU_VIRTUAL_ADDRESS    CommandBuffer;
} D3DKMT_CREATECONTEXT;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] A handle to the device to create the device context on. </p>
</dd>

### -field <b>NodeOrdinal</b>

<dd>
<p>[in] The zero-based index of the node that the context is scheduled on.</p>
</dd>

### -field <b>EngineAffinity</b>

<dd>
<p>[in] The engine affinity for the context.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-createcontextflags.md">D3DDDI_CREATECONTEXTFLAGS</a> structure that indicates, in bit-field flags, how to create the context. </p>
</dd>

### -field <b>pPrivateDriverData</b>

<dd>
<p>[in] A pointer to private data that is passed to the display miniport driver. </p>
</dd>

### -field <b>PrivateDriverDataSize</b>

<dd>
<p>[in] The size, in bytes, of the private data that <b>pPrivateDriverData</b> points to.</p>
</dd>

### -field <b>ClientHint</b>

<dd>
<p>[in] A D3DKMT_CLIENTHINT-typed value that indicates the type of client that creates the context. The following table lists the possible values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DKMT_CLIENTHINT_UNKNOWN (0)</p>
</td>
<td>
<p>The client is unknown.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_CLIENTHINT_OPENGL (1)</p>
</td>
<td>
<p>The client is the OpenGL runtime.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_CLIENTHINT_CDD (2)</p>
</td>
<td>
<p>This value is for internal use only. Do not use.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_CLIENTHINT_DX7 (7)</p>
</td>
<td>
<p>The client is the Microsoft DirectX 7.0 runtime.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_CLIENTHINT_DX8 (8)</p>
</td>
<td>
<p>The client is the DirectX 8.0 runtime.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_CLIENTHINT_DX9 (9)</p>
</td>
<td>
<p>The client is the DirectX 9.0 runtime.</p>
</td>
</tr>
<tr>
<td>
<p>D3DKMT_CLIENTHINT_DX10 (10)</p>
</td>
<td>
<p>The client is the DirectX 10.0 runtime.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>hContext</b>

<dd>
<p>[out] A handle to the device context that the DirectX graphics kernel subsystem (<i>Dxgkrnl.sys</i>) supplied and that is returned from the call to the <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtcreatecontext.md">D3DKMTCreateContext</a> function.</p>
</dd>

### -field <b>pCommandBuffer</b>

<dd>
<p>[out] A pointer to command buffer memory that the OpenGL ICD places commands into. The <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtcreatecontext.md">D3DKMTCreateContext</a> function returns this memory pointer.</p>
</dd>

### -field <b>CommandBufferSize</b>

<dd>
<p>[out] The size, in bytes, of the memory block that <b>pCommandBuffer</b> points to. The <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtcreatecontext.md">D3DKMTCreateContext</a> function returns this size value.</p>
</dd>

### -field <b>pAllocationList</b>

<dd>
<p>[out] An array of <a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-allocationlist.md">D3DDDI_ALLOCATIONLIST</a> structures that the OpenGL ICD inserts referenced allocations in.</p>
<p>The <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtcreatecontext.md">D3DKMTCreateContext</a> function returns this array. </p>
</dd>

### -field <b>AllocationListSize</b>

<dd>
<p>[out] The number of elements in the array of allocations that <b>pAllocationList</b> points to. This quantity of allocations is available when the DirectX graphics kernel subsystem submits the command buffer that is pointed to by <b>pCommandBuffer</b> to the display miniport driver. </p>
<p>The <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtcreatecontext.md">D3DKMTCreateContext</a> function returns this number. </p>
</dd>

### -field <b>pPatchLocationList</b>

<dd>
<p>[out] An array of <a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-patchlocationlist.md">D3DDDI_PATCHLOCATIONLIST</a> structures that the OpenGL ICD inserts patching information in.</p>
<p>The <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtcreatecontext.md">D3DKMTCreateContext</a> function returns this array. </p>
</dd>

### -field <b>PatchLocationListSize</b>

<dd>
<p>[out] The number of elements in the patch-location list that <b>pPatchLocationList</b> points to. This quantity of patch locations is available when the DirectX graphics kernel subsystem submits the command buffer that is pointed to by <b>pCommandBuffer</b> to the display miniport driver. </p>
<p>The <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtcreatecontext.md">D3DKMTCreateContext</a> function returns this number. </p>
</dd>

### -field <b>CommandBuffer</b>

<dd>
<p>[out] A pointer to command buffer memory that the OpenGL ICD places commands into. The <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtcreatecontext.md">D3DKMTCreateContext</a> function returns this memory pointer.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-allocationlist.md">D3DDDI_ALLOCATIONLIST</a>
</dt>
<dt>
<a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-createcontextflags.md">D3DDDI_CREATECONTEXTFLAGS</a>
</dt>
<dt>
<a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-patchlocationlist.md">D3DDDI_PATCHLOCATIONLIST</a>
</dt>
<dt>
<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtcreatecontext.md">D3DKMTCreateContext</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_CREATECONTEXT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
