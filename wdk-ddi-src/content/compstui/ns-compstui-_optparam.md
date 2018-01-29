---
UID : NS:compstui._OPTPARAM
title : _OPTPARAM
author : windows-driver-content
description : An array of OPTPARAM structures is used by CPSUI applications (including printer interface DLLs) for describing all the parameter values associated with a property sheet option. The array's address is included in an OPTTYPE structure.
old-location : print\optparam.htm
old-project : print
ms.assetid : d0cd2867-783c-4a41-a819-e919d4ffc1e3
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : "*POPTPARAM, compstui/POPTPARAM, POPTPARAM structure pointer [Print Devices], print.optparam, _OPTPARAM, POPTPARAM, compstui/OPTPARAM, OPTPARAM structure [Print Devices], OPTPARAM, cpsuifnc_1c22c283-993e-45d7-b0c7-1148eafeb13c.xml"
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : compstui.h
req.include-header : Compstui.h
req.target-type : Windows
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
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*POPTPARAM, OPTPARAM"
---

# _OPTPARAM structure
An array of OPTPARAM structures is used by CPSUI applications (including printer interface DLLs) for describing all the parameter values associated with a <a href="https://msdn.microsoft.com/572330d6-1a1b-46fd-bfb4-be2b0990bca4">property sheet option</a>. The array's address is included in an <a href="..\compstui\ns-compstui-_opttype.md">OPTTYPE</a> structure.

## Syntax
````
typedef struct _OPTPARAM {
  WORD      cbSize;
  BYTE      Flags;
  BYTE      Style;
  LPTSTR    pData;
  ULONG_PTR IconID;
  LPARAM    lParam;
  ULONG_PTR dwReserved[2];
} OPTPARAM, *POPTPARAM;
````

## Members


`cbSize`

Size, in bytes, of the OPTPARAM structure.

`dwReserved`

Reserved, must be initialized to zero.

`Flags`

Optional bit flags that modify the parameter's characteristics. The following flags can be set in any combination:

`IconID`

Usually identifies the icon to be associated with the option parameter, but is sometimes used for other purposes. Use of this member is dependent on the <a href="https://msdn.microsoft.com/3b3c002c-a201-4f81-b208-30864343409b">CPSUI option type</a>.

`lParam`

Use of this member is dependent on the <a href="https://msdn.microsoft.com/3b3c002c-a201-4f81-b208-30864343409b">CPSUI option type</a>.

`pData`

Pointer to the parameter's value. Use of this member is dependent on the <a href="https://msdn.microsoft.com/3b3c002c-a201-4f81-b208-30864343409b">CPSUI option type</a>.

`Style`

Push button style, used only for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562844">TVOT_PUSHBUTTON</a> option type.

## Remarks
If the OPTPF_HIDE flag is set in all the OPTPARAM structures associated with an option, CPSUI hides the entire option.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | compstui.h (include Compstui.h) |