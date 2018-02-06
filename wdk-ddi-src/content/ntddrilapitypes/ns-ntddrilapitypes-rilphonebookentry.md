---
UID: NS:ntddrilapitypes.RILPHONEBOOKENTRY
title: RILPHONEBOOKENTRY
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilphonebookentry.htm
old-project: netvista
ms.assetid: 2741d992-624a-4fd1-a1b5-57fb39c42f84
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: ntddrilapitypes/RILPHONEBOOKENTRY, RILPHONEBOOKENTRY, netvista.rilphonebookentry, *LPRILPHONEBOOKENTRY, RILPHONEBOOKENTRY structure [Network Drivers Starting with Windows Vista]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
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
req.lib: 
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ntddrilapitypes.h
apiname:
-	RILPHONEBOOKENTRY
product: Windows
targetos: Windows
req.typenames: "*LPRILPHONEBOOKENTRY, RILPHONEBOOKENTRY"
---

# RILPHONEBOOKENTRY structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILPHONEBOOKENTRY {
  DWORD       cbSize;
  DWORD       dwParams;
  DWORD       dwIndex;
  RILADDRESS  raAddress;
  WCHAR [256] wszText;
  WCHAR [256] wszSecondName;
  DWORD       dwGroupIdCount;
  DWORD [10]  rgdwGroupId;
  DWORD       dwAdditionalNumCount;
  DWORD       dwAdditionalNumSize;
  DWORD       dwAdditionalNumOffset;
  DWORD       dwEmailCount;
  DWORD       dwEmailSize;
  DWORD       dwEmailOffset;
} RILPHONEBOOKENTRY, RILPHONEBOOKENTRY;
````

## Members


`cbSize`



`dwAdditionalNumCount`



`dwAdditionalNumOffset`



`dwAdditionalNumSize`



`dwEmailCount`



`dwEmailOffset`



`dwEmailSize`



`dwGroupIdCount`



`dwIndex`



`dwParams`



`raAddress`



`rgdwGroupId`



`wszSecondName`



`wszText`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |