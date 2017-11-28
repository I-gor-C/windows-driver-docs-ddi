---
UID: NS.dbgeng._STACK_SYM_FRAME_INFO
title: STACK_SYM_FRAME_INFO
author: windows-driver-content
description: Defines stack source information for an extended stack frame.
old-location: debugger\stack_sym_frame_info.htm
old-project: debugger
ms.assetid: 1DE23CF6-970E-4BDE-9BEC-CAC0640B257A
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STACK_SYM_FRAME_INFO, STACK_SYM_FRAME_INFO, *PSTACK_SYM_FRAME_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STACK_SYM_FRAME_INFO
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
req.iface: IDebugSystemObjects4
---

# STACK_SYM_FRAME_INFO structure



## -description
<p>Defines stack source information for an extended stack frame. </p>


## -syntax

````
typedef struct _STACK_SYM_FRAME_INFO {
  DEBUG_STACK_FRAME_EX StackFrameEx;
  STACK_SRC_INFO       SrcInfo;
} STACK_SYM_FRAME_INFO, *PSTACK_SYM_FRAME_INFO;
````


## -struct-fields
<dl>

### -field <b>StackFrameEx</b>

<dd>
<p>A stack frame as a <a href="https://msdn.microsoft.com/library/windows/hardware/dn818561">DEBUG_STACK_FRAME_EX</a> structure. </p>
</dd>

### -field <b>SrcInfo</b>

<dd>
<p>Stack source information as a <a href="..\dbgeng\ns-dbgeng--stack-src-info.md">STACK_SRC_INFO</a> structure.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn818561">DEBUG_STACK_FRAME_EX</a>
</dt>
<dt>
<a href="..\dbgeng\ns-dbgeng--stack-src-info.md">STACK_SRC_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20STACK_SYM_FRAME_INFO structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
