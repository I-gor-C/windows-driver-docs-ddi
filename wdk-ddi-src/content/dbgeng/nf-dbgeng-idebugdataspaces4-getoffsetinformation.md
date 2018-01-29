---
UID : NF:dbgeng.IDebugDataSpaces4.GetOffsetInformation
title : IDebugDataSpaces4::GetOffsetInformation method
author : windows-driver-content
description : The GetOffsetInformation method provides general information about an address in a process's data space.
old-location : debugger\getoffsetinformation.htm
old-project : debugger
ms.assetid : 5ef00c92-7b32-473a-8401-4c02e864c181
ms.author : windowsdriverdev
ms.date : 1/19/2018
ms.keywords : IDebugDataSpaces4, GetOffsetInformation method [Windows Debugging], IDebugDataSpaces4 interface [Windows Debugging], GetOffsetInformation method, GetOffsetInformation method [Windows Debugging], IDebugDataSpaces4 interface, IDebugDataSpaces_c434b12b-78ff-4f6a-ac69-6069dd273ba8.xml, dbgeng/IDebugDataSpaces4::GetOffsetInformation, IDebugDataSpaces4::GetOffsetInformation, debugger.getoffsetinformation, GetOffsetInformation
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : dbgeng.h
req.include-header : Dbgeng.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : dbgeng.h
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
---


# GetOffsetInformation method
The <b>GetOffsetInformation</b> method provides general information about an address in a process's data space.

## Syntax

````
HRESULT GetOffsetInformation(
  [in]            ULONG   Space,
  [in]            ULONG   Which,
  [in]            ULONG64 Offset,
  [out, optional] PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  InfoSize
);
````

## Parameters

`Space`

Specifies the data space to which the <i>Offset </i>parameter applies.  The allowed values depend on the <i>Which</i> parameter.

`Which`

Specifies which information about the data is being queried.  This determines the possible values for <i>Space</i> and the type of the data returned in <i>Buffer</i>.  Possible values are:

`Offset`

Specifies the offset in the target's data space for which the information is returned.

`Buffer`

Specifies the buffer to receive the information.  The type of the data returned depends on the value of <i>Which</i>.  If <i>Buffer</i> is <b>NULL</b>, this information is not returned.

`BufferSize`

Specifies the size, in bytes, of the <i>Buffer </i>buffer.

`InfoSize`

Receives the size, in bytes, of the information that is returned.  If <i>InfoSize</i> is <b>NULL</b>, this information is not returned.


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


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h (include Dbgeng.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |