---
UID: NF.wdm.ASSERTMSG
title: ASSERTMSG
author: windows-driver-content
description: ASSERTMSG tests an expression. If the expression is false, it breaks into the kernel debugger and sends it the specified message.
old-location: devtest\assertmsg.htm
old-project: devtest
ms.assetid: 88c0cd30-607b-48f4-b2b6-3c21be1ce31a
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: ASSERTMSG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows 2000 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ASSERTMSG
req.alt-loc: ntddk.h
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

# ASSERTMSG function



## -description
<p><b>ASSERTMSG</b> tests an expression. If the expression is false, it breaks into the kernel debugger and sends it the specified message.</p>


## -syntax

````
VOID ASSERTMSG(
    Message,
    Expression
);
````


## -parameters
<dl>

### -param <i>Message</i> 

<dd>
<p>Specifies the null-delimited string to be displayed by the debugger.</p>
</dd>

### -param <i>Expression</i> 

<dd>
<p>Specifies any logical expression.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>ASSERTMSG</b> is identical to <b>ASSERT</b>, except that it sends an additional message to the debugger.</p>

<p>This macro will only be included in your binary if your code is compiled in a Debug configuration. Once your driver is built, <b>ASSERTMSG</b> will work properly regardless of whether your driver is run on the checked build or on the free build of Windows. </p>

<p>If <i>Expression</i> evaluates to <b>TRUE</b>, this routine has no effect.</p>

<p>If <i>Expression</i> evaluates to <b>FALSE</b>, a message is displayed in the Debugger Command window. The message contains the source-code string of <i>Expression</i>, as well as the path of the source-code file and the line number of the instruction that called the macro. In this event, <b>ASSERTMSG</b> can be ignored and the process or thread in which <b>ASSERTMSG</b> occurred can be terminated. Alternatively, the debugger can be used to analyze the situation or to edit memory. If <b>ASSERTMSG</b> is ignored, execution continues as if the <b>g (Go)</b> command was entered.</p>

<p><b>ASSERTMSG</b> is identical to <b>ASSERT</b>, except that it sends an additional message to the debugger.</p>

<p>This macro will only be included in your binary if your code is compiled in a Debug configuration. Once your driver is built, <b>ASSERTMSG</b> will work properly regardless of whether your driver is run on the checked build or on the free build of Windows. </p>

<p>If <i>Expression</i> evaluates to <b>TRUE</b>, this routine has no effect.</p>

<p>If <i>Expression</i> evaluates to <b>FALSE</b>, a message is displayed in the Debugger Command window. The message contains the source-code string of <i>Expression</i>, as well as the path of the source-code file and the line number of the instruction that called the macro. In this event, <b>ASSERTMSG</b> can be ignored and the process or thread in which <b>ASSERTMSG</b> occurred can be terminated. Alternatively, the debugger can be used to analyze the situation or to edit memory. If <b>ASSERTMSG</b> is ignored, execution continues as if the <b>g (Go)</b> command was entered.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows 2000 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Wdm.h or Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542107">ASSERT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [devtest\devtest]:%20ASSERTMSG function%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
