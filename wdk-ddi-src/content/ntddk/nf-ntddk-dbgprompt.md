---
UID: NF:ntddk.DbgPrompt
title: DbgPrompt function
author: windows-driver-content
description: The DbgPrompt routine displays a caller-specified user prompt string on the kernel debugger's display device and obtains a user response string.
old-location: devtest\dbgprompt.htm
old-project: devtest
ms.assetid: 4bb44aab-7032-4cc7-89e3-6ac3bee233d3
ms.author: windowsdriverdev
ms.date: 1/10/2018
ms.keywords: DbgPrompt
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DbgPrompt
req.alt-loc: NtDll.dll,NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtDll.lib (user mode); NtosKrnl.lib (kernel mode)
req.dll: NtDll.dll (user mode); NtosKrnl.exe (kernel mode)
req.irql: <= DIRQL
req.typenames: WHEA_RAW_DATA_FORMAT, *PWHEA_RAW_DATA_FORMAT
---


# DbgPrompt function
The <b>DbgPrompt</b> routine displays a caller-specified user prompt string on the kernel debugger's display device and obtains a user response string.

## Syntax

````
ULONG DbgPrompt(
  _In_  PCCH  Prompt,
  _Out_ PCHAR Response,
  _In_  ULONG MaximumResponseLength
);
````

## Parameters

`Prompt`

A pointer to a NULL-terminated constant character string that the debugger will display as a user prompt. The maximum size of this string is 512 characters.

`Response`

A pointer to a character array buffer that receives the user's response, including a terminating newline character. The maximum size of this buffer is 512 characters.

`Length`




## Return Value

<b>DbgPrompt</b> returns the number of characters that the <i>Response</i> buffer received, including the terminating newline character. <b>DbgPrompt</b> returns zero if it receives no characters.

## Remarks

The <b>DbgPrompt</b> routine displays the specified prompt string on the kernel debugger's display device and then reads a line of user input text. 

After <b>DbgPrompt</b> returns, the <i>Response</i> buffer contains the user's response, including the terminating newline character. The user response string is not NULL-terminated.

The following code example asks if the user wants to continue and accepts the letter "y" for yes and the letter "n" for no.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | ntddk.h (include Ntddk.h) |
| **Library** | NtDll.lib (user mode); NtosKrnl.lib (kernel mode) |
| **DLL** | NtDll.dll (user mode); NtosKrnl.exe (kernel mode) |
| **IRQL** | <= DIRQL |