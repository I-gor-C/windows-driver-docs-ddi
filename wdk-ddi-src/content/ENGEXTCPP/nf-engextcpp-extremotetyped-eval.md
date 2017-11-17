---
UID: NF.engextcpp.ExtRemoteTyped.Eval
title: ExtRemoteTyped::Eval
author: windows-driver-content
description: The Eval method returns typed data that is the result of evaluating an expression.
old-location: debugger\extremotetyped_eval.htm
ms.assetid: f54c7dfd-1997-4056-b20a-94438552aeca
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: engextcpp.hpp
req.include-header: Engextcpp.hpp
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExtRemoteTyped.Eval
req.alt-loc: engextcpp.hpp
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
ms.keywords: ExtRemoteTyped, Eval, ExtRemoteTyped::Eval
req.iface: ExtRemoteTyped
---

# ExtRemoteTyped::Eval method



## -description
<p>The <b>Eval</b> method returns typed data that is the result of evaluating an expression.</p>


## -syntax

````
ExtRemoteData Eval(
  [in] PCSTR Expr
);
````


## -parameters
<dl>

### -param <i>Expr</i> [in]

<dd>
<p>The expression to evaluate. <i>Expr</i> is evaluated using the default expression evaluator.</p>
</dd>
</dl>

## -returns
<p><b>Eval</b> returns a new <b>ExtRemoteData</b> object that represents the typed data that is the result of evaluating the expression.</p>

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
<dt>Engextcpp.hpp (include Engextcpp.hpp)</dt>
</dl>
</td>
</tr>
</table>