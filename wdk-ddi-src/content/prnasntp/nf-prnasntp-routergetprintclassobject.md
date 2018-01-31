---
UID : NF:prnasntp.RouterGetPrintClassObject
title : RouterGetPrintClassObject function
author : windows-driver-content
description : The RouterGetPrintClassObject function enumerates the list of print providers, searching for the print provider with the specified name and interface ID.
old-location : print\routergetprintclassobject.htm
old-project : print
ms.assetid : e2df591d-59bd-4aae-ac1b-8fdf01da3ea7
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RouterGetPrintClassObject function [Print Devices], prnasntp/RouterGetPrintClassObject, print.routergetprintclassobject, spoolfnc_ffe877d1-cb3e-49f5-a5b5-5da7c5cb9148.xml, RouterGetPrintClassObject
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : prnasntp.h
req.include-header : Prnasntp.h
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
req.lib : Spoolss.lib
req.dll : Spoolss.dll
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : USERDATA, *PUSERDATA
req.product : Windows 10 or later.
---


# RouterGetPrintClassObject function
The <code>RouterGetPrintClassObject</code> function enumerates the list of print providers, searching for the print provider with the specified name and interface ID.

## Syntax

````
HRESULT RouterGetPrintClassObject(
  _In_  PCWSTR pPrinter,
  _In_  REFIID riid,
  _Out_ VOID   **ppv
);
````

## Parameters

`pPrinter`

A pointer to a null-terminated string that contains the name of the printer or print server.

`riid`

The identifier of the requested COM interface.

`ppv`

A pointer to a variable that supplies the address of the COM interface requested in the <i>iid</i> parameter.


## Return Value

This function returns S_OK on success, and a standard COM error code otherwise.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | prnasntp.h (include Prnasntp.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |