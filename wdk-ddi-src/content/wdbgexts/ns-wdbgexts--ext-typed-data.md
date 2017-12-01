---
UID: NS.wdbgexts._EXT_TYPED_DATA
title: EXT_TYPED_DATA
author: windows-driver-content
description: The EXT_TYPED_DATA structure is passed to and returned from the DEBUG_REQUEST_EXT_TYPED_DATA_ANSI Request operation. It contains the input and output parameters for the operation as well as specifying which particular suboperation to perform.
old-location: debugger\ext_typed_data.htm
old-project: debugger
ms.assetid: 99abb7b6-3e20-4875-b257-c3fc4146e392
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: EXT_TYPED_DATA, EXT_TYPED_DATA, *PEXT_TYPED_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdbgexts.h
req.include-header: WdbgExts.h, DbgEng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EXT_TYPED_DATA
req.alt-loc: wdbgexts.h
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
req.product: Windows 10 or later.
---

# EXT_TYPED_DATA structure



## -description
<p>The EXT_TYPED_DATA structure is passed to and returned from the <a href="https://msdn.microsoft.com/ac883bc8-3956-4bc3-a11e-b6e036305329">DEBUG_REQUEST_EXT_TYPED_DATA_ANSI </a>
<a href="debugger.request">Request</a> operation. It contains the input and output parameters for the operation as well as specifying which particular suboperation to perform.</p>


## -syntax

````
typedef struct _EXT_TYPED_DATA {
  EXT_TDOP         Operation;
  ULONG            Flags;
  DEBUG_TYPED_DATA InData;
  DEBUG_TYPED_DATA OutData;
  ULONG            InStrIndex;
  ULONG            In32;
  ULONG            Out32;
  ULONG64          In64;
  ULONG64          Out64;
  ULONG            StrBufferIndex;
  ULONG            StrBufferChars;
  ULONG            StrCharsNeeded;
  ULONG            DataBufferIndex;
  ULONG            DataBufferBytes;
  ULONG            DataBytesNeeded;
  HRESULT          Status;
  ULONG64          Reserved[8];
} EXT_TYPED_DATA, *PEXT_TYPED_DATA;
````


## -struct-fields
<dl>

### -field <b>Operation</b>

<dd>
<p>Specifies which suboperation the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541547">DEBUG_REQUEST_EXT_TYPED_DATA_ANSI</a>
<a href="debugger.request">Request</a> operation should perform. The interpretation of some of the other members depends on <b>Operation</b>. For a list of possible suboperations, see <a href="..\wdbgexts\ne-wdbgexts--ext-tdop.md">EXT_TDOP</a>.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Specifies the bit flags describing the target's memory in which the data resides. If no flags are present, the data is considered to be in virtual memory. One of the following flags may be present:</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>EXT_TDF_PHYSICAL_DEFAULT</p>
</td>
<td>
<p>The typed data is in physical memory, and this physical memory uses the default memory caching.</p>
</td>
</tr>
<tr>
<td>
<p>EXT_TDF_PHYSICAL_CACHED</p>
</td>
<td>
<p>The typed data is in physical memory, and this physical memory is cached.</p>
</td>
</tr>
<tr>
<td>
<p>EXT_TDF_PHYSICAL_UNCACHED</p>
</td>
<td>
<p>The typed data is in physical memory, and this physical memory is uncached.</p>
</td>
</tr>
<tr>
<td>
<p>EXT_TDF_PHYSICAL_WRITE_COMBINED</p>
</td>
<td>
<p>The typed data is in physical memory, and this physical memory is write-combined.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>InData</b>

<dd>
<p>Specifies typed data to be used as input to the operation. For details about this structure, see <a href="..\wdbgexts\ns-wdbgexts--debug-typed-data.md">DEBUG_TYPED_DATA</a>.</p>
<p>The interpretation of <b>InData</b> depends on the value of <b>Operation</b>.</p>
</dd>

### -field <b>OutData</b>

<dd>
<p>Receives typed data as output from the operation. Any suboperation that returns typed data to <b>OutData</b> initially copies the contents of <b>InData</b> to <b>OutData</b>, then modifies <b>OutData</b> in place, so that the input parameters in <b>InData</b> are also present in <b>OutData</b>. For details about this structure, see <a href="..\wdbgexts\ns-wdbgexts--debug-typed-data.md">DEBUG_TYPED_DATA</a>.</p>
<p>The interpretation of <b>OutData</b> depends on the value of <b>Operation</b>.</p>
</dd>

### -field <b>InStrIndex</b>

<dd>
<p>Specifies the position of an ANSI string to be used as input to the operation. <b>InStrIndex</b> can be zero to indicate that the input parameters do not include an ANSI string.</p>
<p>The position of the string is relative to the base address of this EXT_TYPED_DATA structure. The string must follow this structure, so <b>InStrIndex</b> must be greater than the size of this structure. The string is part of the input to the operation and <b>InStrIndex</b> must be smaller than <i>InBufferSize</i>, the size of the input buffer passed to <a href="debugger.request">Request</a>.</p>
<p>The interpretation of the string depends on the value of <b>Operation</b>.</p>
</dd>

### -field <b>In32</b>

<dd>
<p>Specifies a 32-bit parameter to be used as input to the operation.</p>
<p>The interpretation of <b>In32</b> depends on the value of <b>Operation</b>.</p>
</dd>

### -field <b>Out32</b>

<dd>
<p>Receives a 32-bit value as output from the operation.</p>
<p>The interpretation of <b>Out32</b> depends on the value of <b>Operation</b>.</p>
</dd>

### -field <b>In64</b>

<dd>
<p>Specifies a 64-bit parameter to be used as input to the operation.</p>
<p>The interpretation of <b>In64</b> depends on the value of <b>Operation</b>.</p>
</dd>

### -field <b>Out64</b>

<dd>
<p>Receives a 64-bit value as output from the operation.</p>
<p>The interpretation of <b>Out64</b> depends on the value of <b>Operation</b>.</p>
</dd>

### -field <b>StrBufferIndex</b>

<dd>
<p>Specifies the position to return an ANSI string as output from the operation. <b>StrBufferIndex</b> can be zero if no ANSI string is to be received from the operation.</p>
<p>The position of the string is relative to the base address of the returned EXT_TYPED_DATA structure. The string must follow the structure, so <b>StrBufferIndex</b> must be greater than the size of this structure. The string is part of the output from the suboperation, and <b>StrBufferIndex</b> plus <b>StrBufferChars</b> must be smaller than <i>OutBufferSize</i>, the size of the output buffer passed to <a href="debugger.request">Request</a>.</p>
<p>The interpretation of the string depends on the value of <b>Operation</b>.</p>
</dd>

### -field <b>StrBufferChars</b>

<dd>
<p>Specifies the size in characters of the ANSI string buffer specified by <b>StrBufferIndex</b>.</p>
</dd>

### -field <b>StrCharsNeeded</b>

<dd>
<p>Receives the number of characters needed by the string buffer specified by <b>StrBufferIndex</b>.</p>
</dd>

### -field <b>DataBufferIndex</b>

<dd>
<p>Set to zero.</p>
</dd>

### -field <b>DataBufferBytes</b>

<dd>
<p>Set to zero.</p>
</dd>

### -field <b>DataBytesNeeded</b>

<dd>
<p>Set to zero,</p>
</dd>

### -field <b>Status</b>

<dd>
<p>Receives the status code returned by the operation. This is the same value returned by <a href="debugger.request">Request</a>.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Set to zero.</p>
</dd>
</dl>

## -remarks
<p>The members of this structure are used as the input and output parameters to the <a href="https://msdn.microsoft.com/ac883bc8-3956-4bc3-a11e-b6e036305329">DEBUG_REQUEST_EXT_TYPED_DATA_ANSI </a>
<a href="debugger.request">Request</a> operation. The interpretation of most of the parameters depends on the particular suboperation being performed, as specified by the <b>Operation</b> member.</p>

<p>This structure can optionally specify additional data--using the members <b>InStrIndex</b> and <b>StrBufferIndex</b>--that is included with the structure. This additional data is specified relative to the address of the instance of this structure. When used with the DEBUG_REQUEST_EXT_TYPED_DATA_ANSI <b>Request</b> operation, the additional data is included in the <i>InBuffer</i> and <i>OutBuffer</i> (as appropriate) and should be included in the size of these two buffers.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdbgexts.h (include WdbgExts.h or DbgEng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541547">DEBUG_REQUEST_EXT_TYPED_DATA_ANSI</a>
</dt>
<dt>
<a href="debugger.request">Request</a>
</dt>
<dt>
<a href="..\wdbgexts\ns-wdbgexts--debug-typed-data.md">DEBUG_TYPED_DATA</a>
</dt>
<dt>
<a href="..\wdbgexts\ne-wdbgexts--ext-tdop.md">EXT_TDOP</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20EXT_TYPED_DATA structure%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
