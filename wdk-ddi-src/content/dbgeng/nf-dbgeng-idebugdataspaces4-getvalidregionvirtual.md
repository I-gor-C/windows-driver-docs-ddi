---
UID: NF.dbgeng.IDebugDataSpaces4.GetValidRegionVirtual
title: IDebugDataSpaces4::GetValidRegionVirtual
author: windows-driver-content
description: The GetValidRegionVirtual method locates the first valid region of memory in a specified memory range.
old-location: debugger\getvalidregionvirtual.htm
old-project: debugger
ms.assetid: b580c2ef-94f9-4738-bd00-0d5a4753f71a
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugDataSpaces4, GetValidRegionVirtual, IDebugDataSpaces4::GetValidRegionVirtual
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugDataSpaces4.GetValidRegionVirtual
req.alt-loc: dbgeng.h
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
req.iface: IDebugDataSpaces4
---

# IDebugDataSpaces4::GetValidRegionVirtual method



## -description
<p>The <b>GetValidRegionVirtual</b> method locates the first valid region of memory in a specified memory range.</p>


## -syntax

````
HRESULT GetValidRegionVirtual(
  [in]  ULONG64  Base,
  [in]  ULONG    Size,
  [out] PULONG64 ValidBase,
  [out] PULONG   ValidSize
);
````


## -parameters
<dl>

### -param <i>Base</i> [in]

<dd>
<p>Specifies the address of the beginning of the memory range to search for valid memory.</p>
</dd>

### -param <i>Size</i> [in]

<dd>
<p>Specifies the size, in bytes, of the memory range to search.</p>
</dd>

### -param <i>ValidBase</i> [out]

<dd>
<p>Receives the address of the beginning of the found valid memory.</p>
</dd>

### -param <i>ValidSize</i> [out]

<dd>
<p>Receives the size, in bytes, of the valid memory.</p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugdataspaces4.md">IDebugDataSpaces4</a>
</dt>
<dt>
<a href="debugger.getnextdifferentlyvalidoffsetvirtual">GetNextDifferentlyValidOffsetVirtual</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugDataSpaces4::GetValidRegionVirtual method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
