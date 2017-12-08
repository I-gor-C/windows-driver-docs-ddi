---
UID: NS.d3dukmdt._D3DDDI_PATCHLOCATIONLIST
title: D3DDDI_PATCHLOCATIONLIST
author: windows-driver-content
description: The D3DDDI_PATCHLOCATIONLIST structure describes the location of an allocation to patch (that is, assign a physical address to the allocation).
old-location: display\d3dddi_patchlocationlist.htm
old-project: display
ms.assetid: 88cdbf2d-4b66-47c1-97e1-e3b8377ac526
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_PATCHLOCATIONLIST, D3DDDI_PATCHLOCATIONLIST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_PATCHLOCATIONLIST
req.alt-loc: d3dukmdt.h
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

# D3DDDI_PATCHLOCATIONLIST structure



## -description
<p>The D3DDDI_PATCHLOCATIONLIST structure describes the location of an allocation to patch (that is, assign a physical address to the allocation).</p>


## -syntax

````
typedef struct _D3DDDI_PATCHLOCATIONLIST {
  UINT  AllocationIndex;
  union {
    struct {
      UINT SlotId  :24;
      UINT Reserved  :8;
    };
    UINT   Value;
  };
  UINT  DriverId;
  UINT  AllocationOffset;
  UINT  PatchOffset;
  UINT  SplitOffset;
} D3DDDI_PATCHLOCATIONLIST;
````


## -struct-fields
<dl>

### -field AllocationIndex

<dd>
<p>[in] An index of the element in the allocation list that specifies the allocation that is referenced by the patch location.</p>
</dd>

### -field SlotId

<dd>
<p>[in/out] A UINT that identifies the slot where the allocation will reside. Resources with identical slot identifiers can replace each other.</p>
<p>Setting this member is equivalent to setting bits in the first 24 bits of the 32-bit <b>Value</b> member (0x00FFFFFF). </p>
</dd>

### -field Reserved

<dd>
<p>[in] This member is reserved and should be set to zero. </p>
<p>Setting this member to zero is equivalent to setting the remaining 8 bits (0xFF000000) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field Value

<dd>
<p>[in] A 32-bit value that identifies the location of an allocation to patch.</p>
</dd>

### -field DriverId

<dd>
<p>[in/out] The driver-defined identifier of the allocation specification. </p>
</dd>

### -field AllocationOffset

<dd>
<p>[in/out] The starting offset, in bytes, within the allocation that is referenced. </p>
</dd>

### -field PatchOffset

<dd>
<p>[in/out] The offset, in bytes, into the DMA buffer that must be patched.</p>
</dd>

### -field SplitOffset

<dd>
<p>[in/out] The offset, in bytes, where the DMA buffer must be split if the allocation cannot be brought into video memory.</p>
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
<dt>D3dukmdt.h (include D3dumddi.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createdevice.md">CreateDevice</a>
</dt>
<dt>
<a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-allocationlist.md">D3DDDI_ALLOCATIONLIST</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-createdevice.md">D3DDDIARG_CREATEDEVICE</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddicb-render.md">D3DDDICB_RENDER</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-rendercb.md">pfnRenderCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_PATCHLOCATIONLIST structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
