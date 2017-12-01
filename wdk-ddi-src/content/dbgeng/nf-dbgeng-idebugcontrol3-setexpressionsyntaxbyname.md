---
UID: NF.dbgeng.IDebugControl3.SetExpressionSyntaxByName
title: IDebugControl3::SetExpressionSyntaxByName
author: windows-driver-content
description: The SetExpressionSyntaxByName method sets the syntax that the engine will use to evaluate expressions.
old-location: debugger\setexpressionsyntaxbyname.htm
old-project: debugger
ms.assetid: b9f1618a-e4f7-4eb1-952f-0f565a068dab
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl3, SetExpressionSyntaxByName, IDebugControl3::SetExpressionSyntaxByName
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
req.alt-api: IDebugControl3.SetExpressionSyntaxByName
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
req.iface: IDebugControl3
---

# IDebugControl3::SetExpressionSyntaxByName method



## -description
<p>The <b>SetExpressionSyntaxByName</b>  method sets the syntax that the engine will use to evaluate expressions.</p>


## -syntax

````
HRESULT SetExpressionSyntaxByName(
  [in] PCSTR AbbrevName
);
````


## -parameters
<dl>

### -param <i>AbbrevName</i> [in]

<dd>
<p>Specifies the abbreviated name of the syntax.  It can be one of the following strings:</p>
<p></p>
<dl>

### -param <a id="C__"></a><a id="c__"></a>C++

<dd>
<p>Expressions will be evaluated according to C++ syntax. For details of this syntax, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540372">C++ Numbers and Operators</a>.</p>
</dd>

### -param <a id="MASM"></a><a id="masm"></a>MASM

<dd>
<p>Expressions will be evaluated according to MASM syntax. For details of this syntax, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552157">MASM Numbers and Operators</a>.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The expression syntax is a global setting within the engine, so setting the expression syntax will affect all clients.</p>

<p>The expression syntax of the engine determines how the engine will interpret expressions passed to <a href="debugger.evaluate">Evaluate</a>, <a href="debugger.execute">Execute</a>, and any other method that evaluates an expression.</p>

<p>After the expression syntax has been changed, the engine sends out notification to the <a href="..\dbgeng\nn-dbgeng-idebugeventcallbacks.md">IDebugEventCallbacks</a> callback object registered with each client.  It also passes the DEBUG_CES_EXPRESSION_SYNTAX flag to the <a href="debugger.idebugeventcallbacks_changeenginestate">IDebugEventCallbacks::ChangeEngineState</a> method.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>
</dt>
<dt>
<a href="debugger.getexpressionsyntax">GetExpressionSyntax</a>
</dt>
<dt>
<a href="debugger.setexpressionsyntax">SetExpressionSyntax</a>
</dt>
<dt>
<a href="debugger.evaluate">Evaluate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl3::SetExpressionSyntaxByName method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
