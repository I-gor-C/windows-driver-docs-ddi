---
UID: NF:ntifs.SeTokenIsNoChildProcessRestrictionEnforced
title: SeTokenIsNoChildProcessRestrictionEnforced function
author: windows-driver-content
description: The SeTokenIsNoChildProcessRestrictionEnforced routine determines if the token carries the no child process restriction.
old-location: ifsk\setokenisnochildprocessrestrictionenforced.htm
old-project: ifsk
ms.assetid: 6D214346-8CE6-4E9C-B054-1C72B928ED2B
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: ifsk.setokenisnochildprocessrestrictionenforced, SeTokenIsNoChildProcessRestrictionEnforced function [Installable File System Drivers], ntifs/SeTokenIsNoChildProcessRestrictionEnforced, SeTokenIsNoChildProcessRestrictionEnforced
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10, version 1709.
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
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	DllExport
apilocation:
-	NtosKrnl.exe
apiname:
-	SeTokenIsNoChildProcessRestrictionEnforced
product: Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# SeTokenIsNoChildProcessRestrictionEnforced function
The <b>SeTokenIsNoChildProcessRestrictionEnforced</b> routine determines if the token carries the no child process restriction.

## Syntax

````
BOOLEAN NTKERNELAPI SeTokenIsNoChildProcessRestrictionEnforced(
  _In_      PACCESS_TOKEN Token,
  _Out_opt_ PBOOLEAN      UnlessSecure
);
````

## Parameters

`Token`

Specifies a pointer to the access token.

`UnlessSecure`

Optionally provides a pointer to the value that will
        be set to TRUE when secure process creation is enabled even if
        process creation is restricted.


## Return Value

This routine returns <b>TRUE</b> if <i>Token</i> carries the no child process restriction.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 10, version 1709.  |
| **Target Platform** | Windows |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |