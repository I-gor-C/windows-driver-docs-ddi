---
UID: NF.dbgeng.IDebugControl3.Evaluate
title: IDebugControl3::Evaluate
author: windows-driver-content
description: The Evaluate method evaluates an expression, returning the result.
old-location: debugger\evaluate.htm
ms.assetid: 67b17847-6ab3-4712-9ffc-94f8016e3c34
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugControl.Evaluate,IDebugControl2.Evaluate,IDebugControl3.Evaluate
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
ms.keywords: IDebugControl3, Evaluate, IDebugControl3::Evaluate
req.iface: IDebugControl3
---

# IDebugControl3::Evaluate method



## -description
<p>The <b>Evaluate</b>  method evaluates an expression, returning the result.</p>


## -syntax

````
HRESULT Evaluate(
  [in]            PCSTR        Expression,
  [in]            ULONG        DesiredType,
  [out]           PDEBUG_VALUE Value,
  [out, optional] PULONG       RemainderIndex
);
````


## -parameters
<dl>

### -param <i>Expression</i> [in]

<dd>
<p>Specifies the expression to be evaluated.</p>
</dd>

### -param <i>DesiredType</i> [in]

<dd>
<p>Specifies the desired return type.  Possible values are described in <a href="https://msdn.microsoft.com/library/windows/hardware/ff541719">DEBUG_VALUE</a>; with the addition of DEBUG_VALUE_INVALID, which indicates that the return type should be the expression's natural type.</p>
</dd>

### -param <i>Value</i> [out]

<dd>
<p>Receives the value of the expression.</p>
</dd>

### -param <i>RemainderIndex</i> [out, optional]

<dd>
<p>Receives the index of the first character of the expression not used in the evaluation.  If <i>RemainderIndex</i> is <b>NULL</b>, this information isn't returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>An error occurred while evaluating the expression.  For example, there was a syntax error, an undefined variable, or a division by zero exception.</p>

<p> </p>

## -remarks
<p>Expressions are evaluated by the current <i>expression evaluator</i>.  The engine contains multiple expression evaluators; each supports a different syntax.  The current expression evaluator can be chosen by using <a href="https://msdn.microsoft.com/library/windows/hardware/ff556696">SetExpressionSyntax</a>.</p>

<p>For details of the available expression evaluators and their syntaxes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552280">Numerical Expression Syntax</a>.</p>

<p>If an error occurs while evaluating the expression, returning E_FAIL, the <i>RemainderIndex</i> variable can be used to determine approximately where in the expression the error occurred. </p>

<p>Expressions are evaluated by the current <i>expression evaluator</i>.  The engine contains multiple expression evaluators; each supports a different syntax.  The current expression evaluator can be chosen by using <a href="https://msdn.microsoft.com/library/windows/hardware/ff556696">SetExpressionSyntax</a>.</p>

<p>For details of the available expression evaluators and their syntaxes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552280">Numerical Expression Syntax</a>.</p>

<p>If an error occurs while evaluating the expression, returning E_FAIL, the <i>RemainderIndex</i> variable can be used to determine approximately where in the expression the error occurred. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550508">IDebugControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550512">IDebugControl2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550519">IDebugControl3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546701">GetExpressionSyntax</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556696">SetExpressionSyntax</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556697">SetExpressionSyntaxByName</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::Evaluate method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
