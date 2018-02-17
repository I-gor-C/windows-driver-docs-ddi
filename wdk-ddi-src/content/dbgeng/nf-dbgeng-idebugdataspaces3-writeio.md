---
UID: NF:dbgeng.IDebugDataSpaces3.WriteIo
title: IDebugDataSpaces3::WriteIo method
author: windows-driver-content
description: The WriteIo method writes to the system and bus I/O memory.
old-location: debugger\writeio.htm
old-project: debugger
ms.assetid: 3bc84b15-7c13-4ad9-b9a1-6abd5a7389eb
ms.author: windowsdriverdev
ms.date: 1/19/2018
ms.keywords: dbgeng/IDebugDataSpaces2::WriteIo, dbgeng/IDebugDataSpaces3::WriteIo, dbgeng/IDebugDataSpaces::WriteIo, IDebugDataSpaces3::WriteIo, debugger.writeio, IDebugDataSpaces2, WriteIo method [Windows Debugging], IDebugDataSpaces4::WriteIo, IDebugDataSpaces2::WriteIo, IDebugDataSpaces2 interface [Windows Debugging], WriteIo method, dbgeng/IDebugDataSpaces4::WriteIo, IDebugDataSpaces3 interface [Windows Debugging], WriteIo method, IDebugDataSpaces4 interface [Windows Debugging], WriteIo method, IDebugDataSpaces3, WriteIo method [Windows Debugging], IDebugDataSpaces3 interface, WriteIo method [Windows Debugging], IDebugDataSpaces2 interface, WriteIo method [Windows Debugging], IDebugDataSpaces4 interface, IDebugDataSpaces_d36b33ec-db19-4df1-8813-b77f22705279.xml, WriteIo method [Windows Debugging], IDebugDataSpaces interface, IDebugDataSpaces, IDebugDataSpaces::WriteIo, IDebugDataSpaces interface [Windows Debugging], WriteIo method, WriteIo
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
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: dbgeng.h
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	dbgeng.h
apiname:
-	IDebugDataSpaces.WriteIo
-	IDebugDataSpaces2.WriteIo
-	IDebugDataSpaces3.WriteIo
-	IDebugDataSpaces4.WriteIo
product: Windows
targetos: Windows
req.typenames: "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
---


# WriteIo method
The <b>WriteIo</b> method writes to the system and bus I/O memory.

## Syntax

````
HRESULT WriteIo(
  [in]            ULONG   InterfaceType,
  [in]            ULONG   BusNumber,
  [in]            ULONG   AddressSpace,
  [in]            ULONG64 Offset,
  [in]            PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  BytesWritten
);
````

## Parameters

`InterfaceType`

Specifies the interface type of the I/O bus.  This parameter may take values in the INTERFACE_TYPE enumeration defined in wdm.h.

`BusNumber`

Specifies the system-assigned number of the bus.  This is usually zero, unless the system has more than one bus of the same interface type.

`AddressSpace`

Set to one.

`Offset`

Specifies the location of the requested data.

`Buffer`

Specifies the data to write to the I/O bus.

`BufferSize`

Specifies the size in bytes of the buffer <i>Buffer</i>.  This is the maximum number of bytes that will be written.

`BytesWritten`

Receives the number of bytes written to I/O bus.  If <i>BytesWritten</i> is <b>NULL</b>, this information is not returned.


## Return Value

This method can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>S_OK</b></dt>
</dl>
</td>
<td width="60%">
The method was successful.

</td>
</tr>
</table>

## Remarks

This method is only available in kernel-mode debugging.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | dbgeng.h (include Dbgeng.h) |
| **Library** | dbgeng.h |