---
UID : NS:ntddrilapitypes.RILDELETEPHONEBOOKENTRYPARAMS
title : RILDELETEPHONEBOOKENTRYPARAMS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rildeletephonebookentryparams.htm
old-project : netvista
ms.assetid : 1a372468-2bad-44d4-a19a-d3b517b7ed7b
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : "*LPRILDELETEPHONEBOOKENTRYPARAMS, ntddrilapitypes/RILDELETEPHONEBOOKENTRYPARAMS, RILDELETEPHONEBOOKENTRYPARAMS, RILDELETEPHONEBOOKENTRYPARAMS structure [Network Drivers Starting with Windows Vista], netvista.rildeletephonebookentryparams"
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddrilapitypes.h
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
req.typenames : "*LPRILDELETEPHONEBOOKENTRYPARAMS, RILDELETEPHONEBOOKENTRYPARAMS"
---

# RILDELETEPHONEBOOKENTRYPARAMS structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILDELETEPHONEBOOKENTRYPARAMS {
  HUICCAPP                    hUiccApp;
  RILPHONEENTRYSTORELOCATION  dwStoreLocation;
  DWORD                       dwIndex;
  BOOL                        fHasLockVerification;
  RILUICCLOCKCREDENTIAL       lockVerification;
} RILDELETEPHONEBOOKENTRYPARAMS, RILDELETEPHONEBOOKENTRYPARAMS;
````

## Members


`dwIndex`



`dwStoreLocation`



`fHasLockVerification`



`hUiccApp`



`lockVerification`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |