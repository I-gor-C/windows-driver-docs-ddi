---
UID: NF.dbgeng.DebugCreateEx
title: DebugCreateEx
author: windows-driver-content
description: The DebugCreateEx function creates a new client object and returns an interface pointer to it.
old-location: debugger\debugcreateex.htm
old-project: debugger
ms.assetid: 851A9461-E085-4BDA-BB69-603F6932BFA6
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DebugCreateEx
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
req.alt-api: DebugCreateEx
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
req.iface: 
---

# DebugCreateEx function



## -description
<p>The <b>DebugCreateEx</b> function creates a new <a href="https://msdn.microsoft.com/173a67f1-093e-4462-8e2c-41d0f10106d0">client object</a> and returns an interface pointer to it.</p>


## -syntax

````
HRESULT DebugCreateEx(
  _In_  REFIID InterfaceId,
  _In_  DWORD  DbgEngOptions,
  _Out_ PVOID  *Interface
);
````


## -parameters
<dl>

### -param <i>InterfaceId</i> [in]

<dd>
<p>Specifies the interface identifier (IID) of the desired debugger engine client interface.  This is the type of the interface that will be returned in <i>Interface</i>. For information about the interface identifier, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560088">Using Client Objects</a>.</p>
</dd>

### -param <i>DbgEngOptions</i> [in]

<dd>
<p>Supplies debugger option flags.</p>
</dd>

### -param <i>Interface</i> [out]

<dd>
<p>Receives an interface pointer for the new client.  The type of this interface is specified by <i>InterfaceId</i>.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The function was successful.</p><dl>
<dt><b>E_NOINTERFACE </b></dt>
</dl><p>The client object doesn't implement the specified interface.</p>

<p> </p>

## -remarks
<p>The parameters passed to <b>DebugCreateEx</b> are the same as those passed to <b>IUnknown::QueryInterface</b>, and they are treated the same way.</p>

<p>As with <b>IUnknown::QueryInterface</b>, when the returned interface is no longer needed, its <b>IUnknown::Release</b> method should be called.</p>

<p>The parameters passed to <b>DebugCreateEx</b> are the same as those passed to <b>IUnknown::QueryInterface</b>, and they are treated the same way.</p>

<p>As with <b>IUnknown::QueryInterface</b>, when the returned interface is no longer needed, its <b>IUnknown::Release</b> method should be called.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539137">Client Functions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539140">Client Objects</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20DebugCreateEx function%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
