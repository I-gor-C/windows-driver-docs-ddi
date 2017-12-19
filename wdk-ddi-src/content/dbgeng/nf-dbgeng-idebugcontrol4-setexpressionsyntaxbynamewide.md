---
UID: NF.dbgeng.IDebugControl4.SetExpressionSyntaxByNameWide
title: IDebugControl4::SetExpressionSyntaxByNameWide method
author: windows-driver-content
description: The SetExpressionSyntaxByNameWide method sets the syntax that the engine will use to evaluate expressions.
old-location: debugger\setexpressionsyntaxbynamewide.htm
old-project: Debugger
ms.assetid: cad4ee84-333a-49ff-a087-da0e36b87989
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IDebugControl4, IDebugControl4::SetExpressionSyntaxByNameWide, SetExpressionSyntaxByNameWide
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
req.alt-api: IDebugControl4.SetExpressionSyntaxByNameWide
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

# IDebugControl4::SetExpressionSyntaxByNameWide method



## -description
The  <b>SetExpressionSyntaxByNameWide</b> method sets the syntax that the engine will use to evaluate expressions.



## -syntax

````
HRESULT SetExpressionSyntaxByNameWide(
  [in] PCWSTR AbbrevName
);
````


## -parameters

### -param AbbrevName [in]

Specifies the abbreviated name of the syntax.  It can be one of the following strings:




### -param C++

Expressions will be evaluated according to C++ syntax. For details of this syntax, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540372">C++ Numbers and Operators</a>.


### -param MASM

Expressions will be evaluated according to MASM syntax. For details of this syntax, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552157">MASM Numbers and Operators</a>.

</dd>
</dl>

## -returns
This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.

 


## -remarks
The expression syntax is a global setting within the engine, so setting the expression syntax will affect all clients.

The expression syntax of the engine determines how the engine will interpret expressions passed to <a href="debugger.evaluate">Evaluate</a>, <a href="debugger.execute">Execute</a>, and any other method that evaluates an expression.

After the expression syntax has been changed, the engine sends out notification to the <a href="..\dbgeng\nn-dbgeng-idebugeventcallbacks.md">IDebugEventCallbacks</a> callback object registered with each client.  It also passes the DEBUG_CES_EXPRESSION_SYNTAX flag to the <a href="debugger.idebugeventcallbacks_changeenginestate">IDebugEventCallbacks::ChangeEngineState</a> method.


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
<a href="..\dbgeng\nn-dbgeng-idebugcontrol4.md">IDebugControl4</a>
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
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20IDebugControl4::SetExpressionSyntaxByNameWide method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

