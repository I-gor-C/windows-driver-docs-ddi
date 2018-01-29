---
UID : NS:compstui._CPSUICBPARAM
title : _CPSUICBPARAM
author : windows-driver-content
description : The CPSUICBPARAM structure is used as the input parameter to _CPSUICALLBACK-typed callback functions.
old-location : print\cpsuicbparam.htm
old-project : print
ms.assetid : b5545efa-6cb4-41d0-9338-be9a269fa193
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : cpsuifnc_9e2d49ae-ecb6-4979-aacd-7dd954034e92.xml, print.cpsuicbparam, CPSUICBPARAM, PCPSUICBPARAM, compstui/CPSUICBPARAM, compstui/PCPSUICBPARAM, *PCPSUICBPARAM, CPSUICBPARAM structure [Print Devices], _CPSUICBPARAM, PCPSUICBPARAM structure pointer [Print Devices]
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
req.typenames : CPSUICBPARAM, *PCPSUICBPARAM
---

# _CPSUICBPARAM structure
The CPSUICBPARAM structure is used as the input parameter to <a href="..\compstui\nc-compstui-_cpsuicallback.md">_CPSUICALLBACK</a>-typed callback functions.

## Syntax
````
typedef struct _CPSUICBPARAM {
  WORD      cbSize;
  WORD      Reason;
  HWND      hDlg;
  POPTITEM  pOptItem;
  WORD      cOptItem;
  WORD      Flags;
  POPTITEM  pCurItem;
  union {
    LONG   OldSel;
    LPTSTR pOldSel;
  };
  ULONG_PTR UserData;
  ULONG_PTR Result;
} CPSUICBPARAM, *PCPSUICBPARAM;
````

## Members


`cbSize`

CPSUI-supplied size, in bytes, of the CPSUICBPARAM structure.

`cOptItem`

CPSUI-supplied number of OPTITEM structures in the array pointed to by <b>pOptItem</b>. This is the same number that the application previously supplied in a <a href="..\compstui\ns-compstui-_compropsheetui.md">COMPROPSHEETUI</a> structure.

`DUMMYUNIONNAME`



`Flags`

CPSUI-supplied flags. This is the same set of flags that the application previously supplied in a <a href="..\compstui\ns-compstui-_compropsheetui.md">COMPROPSHEETUI</a> structure.

`hDlg`

CPSUI-supplied handle to the currently active dialog box.

`pCurItem`

CPSUI-supplied pointer to a member of the OPTITEM array pointed to by <b>pOptItem</b>. This array member represents the "current" option, which is the one for which the callback function was called.

`pOptItem`

CPSUI-supplied pointer to an array of <a href="..\compstui\ns-compstui-_optitem.md">OPTITEM</a> structures. This is the same pointer that the application previously supplied in a <a href="..\compstui\ns-compstui-_compropsheetui.md">COMPROPSHEETUI</a> structure.

`Reason`

CPSUI-supplied value indicating the reason it is calling the callback function. This can be one of the following values:

`Result`

Result value supplied by the <a href="..\compstui\nc-compstui-_cpsuicallback.md">_CPSUICALLBACK</a>-typed callback function. By default, CPSUI sets this value to CPSUI_OK. After the callback function returns, CPSUI calls its <a href="https://msdn.microsoft.com/library/windows/hardware/ff546207">ComPropSheet</a> function with a function code of <a href="https://msdn.microsoft.com/library/windows/hardware/ff547087">CPSFUNC_SET_RESULT</a>, supplying the <b>Reason</b> member contents as the result value.

This member is used only if the <b>Reason</b> member is CPSUICB_REASON_APPLYNOW and the callback function does not return CPSUI_ACTION_NO_APPLY_EXIT.

`UserData`

CPSUI-supplied user data. This is the same value that the application previously supplied in a <a href="..\compstui\ns-compstui-_compropsheetui.md">COMPROPSHEETUI</a> structure.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | compstui.h (include Compstui.h) |