---
UID: NF.dbgeng.IDebugControl3.GetExpressionSyntaxNames
title: IDebugControl3::GetExpressionSyntaxNames method
author: windows-driver-content
description: The GetExpressionSyntaxNames method returns the full and abbreviated names of an expression syntax.
old-location: debugger\getexpressionsyntaxnames.htm
old-project: Debugger
ms.assetid: c60b1d7b-b82d-4f59-a076-2122da97a161
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IDebugControl3, IDebugControl3::GetExpressionSyntaxNames, GetExpressionSyntaxNames
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugControl3.GetExpressionSyntaxNames
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
---

# IDebugControl3::GetExpressionSyntaxNames method



## -description
The <b>GetExpressionSyntaxNames</b>  method returns the full and abbreviated names of an expression syntax.



## -syntax

````
HRESULT GetExpressionSyntaxNames(
  [in]            ULONG  Index,
  [out, optional] PSTR   FullNameBuffer,
  [in]            ULONG  FullNameBufferSize,
  [out, optional] PULONG FullNameSize,
  [out, optional] PSTR   AbbrevNameBuffer,
  [in]            ULONG  AbbrevNameBufferSize,
  [out, optional] PULONG AbbrevNameSize
);
````


## -parameters

### -param Index [in]

Specifies the index of the expression syntax.  <i>Index</i> should be between zero and the number of expression syntaxes returned by <a href="debugger.getnumberexpressionsyntaxes">GetNumberExpressionSyntaxes</a> minus one.


### -param FullNameBuffer [out, optional]

Receives the full name of the expression syntax.  If <i>FullNameBuffer</i> is <b>NULL</b>, this information is not returned.


### -param FullNameBufferSize [in]

Specifies the size, in characters, of the buffer <i>FullNameBuffer</i>.


### -param FullNameSize [out, optional]

Receives the size, in characters, of the full name of the expression syntax.  If <i>FullNameSize</i> is <b>NULL</b>, this information is not returned.


### -param AbbrevNameBuffer [out, optional]

Receives the abbreviated name of the expression syntax.  If <i>AbbrevNameBuffer</i> is <b>NULL</b>, this information is not returned.


### -param AbbrevNameBufferSize [in]

Specifies the size, in characters, of the buffer <i>AbbrevNameBufferSize</i>.


### -param AbbrevNameSize [out, optional]

Receives the size, in characters, of the abbreviated name of the expression syntax.  If <i>AbbrevNameSize</i> is <b>NULL</b>, this information is not returned.


## -returns
This method can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.
<dl>
<dt><b>S_FALSE</b></dt>
</dl>The method was successful.  However, either <i>FullNameBufferSize</i> or <i>AbbrevNameBufferSize</i> was smaller than the size of the respective expression syntax name, and the name was truncated to fit inside the buffer.

 


## -remarks
Currently, there are two expression syntaxes, their full names are "Microsoft Assembler expressions" and "C++ source expressions."  The corresponding abbreviated expression syntaxes are "MASM" and "C++."


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>
</dt>
<dt>
<a href="debugger.evaluate">Evaluate</a>
</dt>
<dt>
<a href="debugger.getnumberexpressionsyntaxes">GetNumberExpressionSyntaxes</a>
</dt>
<dt>
<a href="debugger.setexpressionsyntaxbyname">SetExpressionSyntaxByName</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20IDebugControl3::GetExpressionSyntaxNames method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
