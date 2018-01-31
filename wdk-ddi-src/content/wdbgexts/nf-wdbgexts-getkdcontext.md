---
UID : NF:wdbgexts.GetKdContext
title : GetKdContext macro
author : windows-driver-content
description : The GetKdContext function returns the total number of processors and the number of the current processor in the structure ppi points to.
old-location : debugger\getkdcontext.htm
old-project : debugger
ms.assetid : cf795629-cf62-45fa-ad5e-e2eef576bcfd
ms.author : windowsdriverdev
ms.date : 1/19/2018
ms.keywords : GetKdContext function [Windows Debugging], GetKdContext, debugger.getkdcontext, WdbgExts_Ref_951ca10a-3a73-433c-bd95-f054967f0df6.xml, wdbgexts/GetKdContext
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : macro
req.header : wdbgexts.h
req.include-header : Wdbgexts.h, Dbgeng.h
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
req.lib : wdbgexts.h
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : EXT_TDOP
req.product : Windows 10 or later.
---


# GetKdContext function
The <b>GetKdContext</b> function returns the total number of processors and the number of the current processor in the structure <i>ppi</i> points to.

## Syntax

````
ULONG GetKdContext(
   PPROCESSORINFO ppi
);
````

## Parameters

`ppi`

Points to the following structure:
<pre class="syntax" xml:space="preserve"><code>typedef struct _tagPROCESSORINFO {
  USHORT  Processor;           // current processor
  USHORT  NumberProcessors;    // total number of processors
} PROCESSORINFO, *PPROCESSORINFO;</code></pre>


## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdbgexts.h (include Wdbgexts.h, Dbgeng.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |