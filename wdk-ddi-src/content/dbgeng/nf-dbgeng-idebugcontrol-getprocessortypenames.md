---
UID: NF.dbgeng.IDebugControl.GetProcessorTypeNames
title: IDebugControl::GetProcessorTypeNames
author: windows-driver-content
description: The GetProcessorTypeNames method returns the full name and abbreviated name of the specified processor type.
old-location: debugger\getprocessortypenames.htm
old-project: debugger
ms.assetid: cee254a5-7b77-4cab-b02c-69b1f9e3fe02
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugControl, GetProcessorTypeNames, IDebugControl::GetProcessorTypeNames
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
req.alt-api: IDebugControl.GetProcessorTypeNames,IDebugControl2.GetProcessorTypeNames,IDebugControl3.GetProcessorTypeNames
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
req.iface: IDebugControl
---

# IDebugControl::GetProcessorTypeNames method



## -description
<p>The <b>GetProcessorTypeNames</b>  method returns the full name and abbreviated name of the specified processor type.</p>


## -syntax

````
HRESULT GetProcessorTypeNames(
  [in]            ULONG  Type,
  [out, optional] PSTR   FullNameBuffer,
  [in]            ULONG  FullNameBufferSize,
  [out, optional] PULONG FullNameSize,
  [out, optional] PSTR   AbbrevNameBuffer,
  [in]            ULONG  AbbrevNameBufferSize,
  [out, optional] PULONG AbbrevNameSize
);
````


## -parameters
<dl>

### -param Type [in]

<dd>
<p>Specifies the type of the processor whose name is requested.  See <a href="debugger.getactualprocessortype">GetActualProcessorType</a> for a list of possible values.</p>
</dd>

### -param FullNameBuffer [out, optional]

<dd>
<p>Receives the full name of the processor type.  If <i>FullNameBuffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param FullNameBufferSize [in]

<dd>
<p>Specifies the size, in characters, of the buffer that <i>FullNameBuffer</i> specifies.</p>
</dd>

### -param FullNameSize [out, optional]

<dd>
<p>Receives the size in characters of the full name of the processor type.  If <i>FullNameSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param AbbrevNameBuffer [out, optional]

<dd>
<p>Receives the abbreviated name of the processor type.  If <i>AbbrevNameBuffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param AbbrevNameBufferSize [in]

<dd>
<p>Specifies the size, in characters, of the buffer that <i>AbbrevNameBuffer</i> specifies.</p>
</dd>

### -param AbbrevNameSize [out, optional]

<dd>
<p>Receives the size in characters of the abbreviated name of the processor type.  If <i>AbbrevNameSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful.  However, at least one of <i>FullNameBuffer</i> or <i>AbbrevNameBuffer</i> was too small for the corresponding name, so the name was truncated.</p>

<p> </p>

## -remarks
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558860">Target Information</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugcontrol.md">IDebugControl</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol2.md">IDebugControl2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>
</dt>
<dt>
<a href="debugger.getsupportedprocessortypes">GetSupportedProcessorTypes</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::GetProcessorTypeNames method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
