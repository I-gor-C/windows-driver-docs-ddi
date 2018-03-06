---
UID: NF:iddcx.IddCxAdapterInitAsync
title: IddCxAdapterInitAsync function
author: windows-driver-content
description: An asynchronous initiation function called by the driver to create a WDDM graphics adapter.
old-location: display\iddcxadapterinitasync.htm
old-project: display
ms.assetid: c23d0d24-b043-4e39-afd3-abab6bb84769
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IddCxAdapterInitAsync, IddCxAdapterInitAsync method [Display Devices], display.iddcxadapterinitasync, iddcx/IddCxAdapterInitAsync
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.exe
req.dll: 
req.irql: "_Must_inspect_result_"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	iddcx.h
api_name:
-	IddCxAdapterInitAsync
product: Windows
targetos: Windows
req.typenames: 
---


# IddCxAdapterInitAsync function
An asynchronous initiation function called by the driver to create a WDDM graphics adapter.

## Syntax

````
NTSTATUS IddCxAdapterInitAsync(
  _In_  const IDARG_IN_ADAPTER_INIT*  pInArgs,
  _Out_       IDARG_OUT_ADAPTER_INIT* pOutArgs
);
````

## Parameters

`pInArgs`

Input arguments to the function

`pOutArgs`

Output arguments to the function


## Return Value

(NTSTATUS) The method returns S_OK if the operation succeeds. Otherwise, this method returns an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Windows |
| **Header** | iddcx.h |
| **Library** | NtosKrnl.exe |
| **IRQL** | "_Must_inspect_result_" |