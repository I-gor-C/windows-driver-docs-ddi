---
UID : NS:ntnls._NLSTABLEINFO
title : "_NLSTABLEINFO"
author : windows-driver-content
description : Stores the NLS file formats .
old-location : kernel\nlstableinfo.htm
old-project : kernel
ms.assetid : B9E64163-B338-49C9-8167-C36B110AB710
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : PNLSTABLEINFO, PNLSTABLEINFO structure pointer [Kernel-Mode Driver Architecture], *PNLSTABLEINFO, ntnls/NLSTABLEINFO, _NLSTABLEINFO, ntnls/PNLSTABLEINFO, kernel.nlstableinfo, NLSTABLEINFO, NLSTABLEINFO structure [Kernel-Mode Driver Architecture]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntnls.h
req.include-header : 
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
req.typenames : "*PNLSTABLEINFO, NLSTABLEINFO"
---

# _NLSTABLEINFO structure
Stores the NLS file formats .

## Syntax
````
typedef struct _NLSTABLEINFO {
  CPTABLEINFO    OemTableInfo;
  CPTABLEINFO    AnsiTableInfo;
  PUSHORT        UpperCaseTable;
  LowerCaseTable PUSHORT;
} NLSTABLEINFO, *PNLSTABLEINFO;
````

## Members


`AnsiTableInfo`

Specifies an ANSI table.

`LowerCaseTable`



`OemTableInfo`

Specifies OEM table.

`UpperCaseTable`

Specifies an 844 format uppercase table.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntnls.h |