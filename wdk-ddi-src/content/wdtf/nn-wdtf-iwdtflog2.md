---
UID: NN:wdtf.IWDTFLOG2
title: IWDTFLOG2
author: windows-driver-content
description: Defines operations that enable the test case author to add to the WDTF test log.
old-location: dtf\iwdtflog2.htm
old-project: dtf
ms.assetid: e09d0c3d-28a0-4c8d-ac70-9575968cbea1
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IWDTFLOG2, IWDTFLOG2 interface [Windows Device Testing Framework], IWDTFLOG2 interface [Windows Device Testing Framework], described, Microsoft.WDTF.IWDTFLOG2, dtf.iwdtflog2, wdtf/IWDTFLOG2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wdtf.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows XP Professional
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTF.idl
req.max-support: 
req.namespace: Microsoft.WDTF
req.assembly: WDTF.Interop.metadata_dll
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	WDTF.Interop.metadata_dll.dll
api_name:
-	IWDTFLOG2
product:
- Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFLOG2 interface

Defines operations that enable the test case author to add to the WDTF test log.

## Methods

<p>The <b>IWDTFLOG2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFLOG2::EndTestCase](nf-wdtf-iwdtflog2-endtestcase.md) | Marks the end of a test case. |
| [IWDTFLOG2::OutputError](nf-wdtf-iwdtflog2-outputerror.md) | Writes an error entry to the test case log. |
| [IWDTFLOG2::OutputInfo](nf-wdtf-iwdtflog2-outputinfo.md) | Writes an informational entry to the test case log. |
| [IWDTFLOG2::StartTestCase](nf-wdtf-iwdtflog2-starttestcase.md) | Marks the start of a test case. |

## Remarks
You access the logging interface from the <a href="https://msdn.microsoft.com/4c229367-bcdc-466f-ae38-f5c56ae4b840">IWDTF2::Log</a> property.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows XP Professional |
| **Target Platform** | Windows |
| **Header** | wdtf.h |