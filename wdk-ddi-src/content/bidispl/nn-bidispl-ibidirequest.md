---
UID: NN:bidispl.IBidiRequest
title: IBidiRequest
author: windows-driver-content
description: The IBidiRequest interface allows an application or other objects to compose a bidi request.
old-location: print\ibidirequest.htm
old-project: print
ms.assetid: e7b16853-7f1d-45e4-af5e-4ae9cbb9b191
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IBidiRequest, IBidiRequest interface [Print Devices], IBidiRequest interface [Print Devices], described, _win32_IBidiRequest, bidispl/IBidiRequest, gdi.ibidirequest, print.ibidirequest
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: bidispl.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows XP
req.target-min-winversvr: Windows Server 2003
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
req.dll: Bidispl.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	Bidispl.h
api_name:
-	IBidiRequest
product: Windows
targetos: Windows
req.typenames: MPEG2_TRANSPORT_STRIDE, *PMPEG2_TRANSPORT_STRIDE
---

# IBidiRequest interface

The <b>IBidiRequest</b> interface allows an application or other objects to compose a bidi request.

## Methods

<p>The <b>IBidiRequest</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IBidiRequest::GetEnumCount](nf-bidispl-ibidirequest-getenumcount.md) | The GetEnumCount method gets the number of output results from the bidi request. |
| [IBidiRequest::GetOutputData](nf-bidispl-ibidirequest-getoutputdata.md) | The GetOutputData method gets the specified output data coming back from the printer. |
| [IBidiRequest::GetResult](nf-bidispl-ibidirequest-getresult.md) | The GetResult method tells whether the bidi request was successful. |
| [IBidiRequest::SetInputData](nf-bidispl-ibidirequest-setinputdata.md) | The SetInputData method sets the data to send to the printer. |
| [IBidiRequest::SetSchema](nf-bidispl-ibidirequest-setschema.md) | The SetSchema method sets the bidi schema string. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Windows XP |
| **Target Platform** | Windows |
| **Header** | bidispl.h |

## See Also

<a href="https://msdn.microsoft.com/42b5e6cf-b434-4734-86f3-b3b9d15ea468">Print Spooler Components</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff545163">Bidirectional Communication Interfaces</a>



<a href="https://msdn.microsoft.com/b15b1aff-623e-4159-ab0f-ce386a1377eb">Bidirectional Communication Schema</a>