---
UID: NF.dbgeng.IDebugDataSpaces4.ReadImageNtHeaders
title: IDebugDataSpaces4::ReadImageNtHeaders
author: windows-driver-content
description: The ReadImageNtHeaders method returns the NT headers for the specified image loaded in the target.
old-location: debugger\readimagentheaders.htm
old-project: debugger
ms.assetid: 2735aabf-b8b0-4eb1-89a2-4733d0b346ed
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugDataSpaces4, ReadImageNtHeaders, IDebugDataSpaces4::ReadImageNtHeaders
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
req.alt-api: IDebugDataSpaces3.ReadImageNtHeaders,IDebugDataSpaces4.ReadImageNtHeaders
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

# IDebugDataSpaces4::ReadImageNtHeaders method



## -description
<p>The <b>ReadImageNtHeaders</b> method returns the NT headers for the specified image loaded in the target.</p>


## -syntax

````
HRESULT ReadImageNtHeaders(
  [in]  ULONG64             ImageBase,
  [out] PIMAGE_NT_HEADERS64 Headers
);
````


## -parameters
<dl>

### -param <i>ImageBase</i> [in]

<dd>
<p>Specifies the location in the target's virtual address space of the image whose NT headers are being requested.</p>
</dd>

### -param <i>Headers</i> [out]

<dd>
<p>Receives the NT headers for the specified image.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>No NT headers were found for the specified image.</p>

<p> </p>

<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p>

## -remarks
<p>If the image's NT headers are 32-bit, they are automatically converted to 64-bit for consistency.  To determine if the headers were originally 32-bit, look at the value of <b>Headers.OptionalHeader.Magic</b>.  If the value is IMAGE_NT_OPTIONAL_HDR32_MAGIC, the NT headers were originally 32-bit; otherwise the value is IMAGE_NT_OPTIONAL_HDR64_MAGIC, indicating the NT headers were originally 64-bit.</p>

<p>This method will not read ROM headers.</p>

<p>IMAGE_NT_HEADERS64, IMAGE_NT_OPTIONAL_HDR32_MAGIC, and IMAGE_NT_OPTIONAL_HDR64_MAGIC appear in the Microsoft Windows SDK header file winnt.h.  IMAGE_NT_HEADERS64 is the 64-bit equivalent of IMAGE_NT_HEADERS, which is described in the Windows SDK documentation.</p>

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