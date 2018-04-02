---
UID: NN:extsfns.IDebugFailureAnalysis2
title: IDebugFailureAnalysis2
author: windows-driver-content
description: When the !analyze debugger command runs, the analysis engine can load and run extension analysis plug-ins.
old-location: debugger\idebugfailureanalysis2.htm
old-project: debugger
ms.assetid: 0B44FCB9-D23F-4630-9F9A-FBAD46712B14
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: IDebugFailureAnalysis2, IDebugFailureAnalysis2 interface [Windows Debugging], IDebugFailureAnalysis2 interface [Windows Debugging], described, debugger.idebugfailureanalysis2, extsfns/IDebugFailureAnalysis2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: extsfns.h
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	extsfns.h
api_name:
-	IDebugFailureAnalysis2
product: Windows
targetos: Windows
req.typenames: FA_EXTENSION_PLUGIN_PHASE
---

# IDebugFailureAnalysis2 interface

When the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562112">!analyze</a> debugger command runs, the analysis engine can load and run extension analysis plug-ins. The analysis engine creates a <i>DebugFailureAnalysis object</i> to organize data that is related to a particular analysis session.

 An extension analysis plug-in can access a DebugFailureAnalysis object through an <b>IDebugFailureAnalysis2</b> interface. The plug-in can inspect, alter, and enhance the information created by the default analysis. For more information, see <a href="https://msdn.microsoft.com/7648F789-85D5-4247-90DD-2EAA43543483">Writing an Analysis Extension Plug-in to Extend !analyze</a>.

## Methods

<p>The <b>IDebugFailureAnalysis2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugFailureAnalysis2::AddBuffer](nf-extsfns-idebugfailureanalysis2-addbuffer.md) | The AddBuffer method adds a new FA entry to a DebugFailureAnalysis object, and writes the bytes from a specified buffer to the data block of the new FA entry. |
| [IDebugFailureAnalysis2::AddExtensionCommand](nf-extsfns-idebugfailureanalysis2-addextensioncommand.md) | The AddExtensionCommand method adds a new FA entry to a DebugFailureAnalysis object and sets the data block of the FA entry to a specified debugger command. |
| [IDebugFailureAnalysis2::AddString](nf-extsfns-idebugfailureanalysis2-addstring.md) | The AddExtensionCommand method adds a new FA entry to a DebugFailureAnalysis object and sets the data block of the FA entry to a specified debugger command. |
| [IDebugFailureAnalysis2::AddUlong](nf-extsfns-idebugfailureanalysis2-addulong.md) | The AddUlong method adds a new FA entry to a DebugFailureAnalysis object and sets the data block of the FA entry to a specified ULONG value. |
| [IDebugFailureAnalysis2::AddUlong64](nf-extsfns-idebugfailureanalysis2-addulong64.md) | The AddUlong64 method adds a new FA entry to a DebugFailureAnalysis object and sets the data block of the FA entry to a specified 64-bit value. |
| [IDebugFailureAnalysis2::Get](nf-extsfns-idebugfailureanalysis2-get.md) | The Get method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. |
| [IDebugFailureAnalysis2::GetBuffer](nf-extsfns-idebugfailureanalysis2-getbuffer.md) | The GetBuffer method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it gets the entry's data block. |
| [IDebugFailureAnalysis2::GetDebugFATagControl](nf-extsfns-idebugfailureanalysis2-getdebugfatagcontrol.md) | The GetDebugFATagControl method gets a pointer to an IDebugFAEntryTags interface, which provides access to the tags in a DebugFailureAnalysisTags object. |
| [IDebugFailureAnalysis2::GetFailureClass](nf-extsfns-idebugfailureanalysis2-getfailureclass.md) | The GetFailureClass method gets the failure class of a DebugFailureAnalysis object. The failure class indicates whether the debugging session that created the DebugFailureAnalysis object is a kernel mode session or a user mode session. |
| [IDebugFailureAnalysis2::GetFailureCode](nf-extsfns-idebugfailureanalysis2-getfailurecode.md) | The GetFailureCode method gets the bug check code or exception code of a DebugFailureAnalysis object. |
| [IDebugFailureAnalysis2::GetFailureType](nf-extsfns-idebugfailureanalysis2-getfailuretype.md) | The GetFailureType method gets the failure type of a DebugFailureAnalysis object. The failure type indicates whether the code being analyzed was running in kernel mode or user mode. |
| [IDebugFailureAnalysis2::GetNext](nf-extsfns-idebugfailureanalysis2-getnext.md) | The GetNext method searches a DebugFailureAnalysis object for the next FA entry, after a given FA entry, that satisfies conditions specified by the Tag and TagMask parameters. |
| [IDebugFailureAnalysis2::GetString](nf-extsfns-idebugfailureanalysis2-getstring.md) | The GetString method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it gets the ANSI string value from the entry's data block. |
| [IDebugFailureAnalysis2::GetUlong](nf-extsfns-idebugfailureanalysis2-getulong.md) | The GetString method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it gets the ANSI string value from the entry's data block. |
| [IDebugFailureAnalysis2::GetUlong64](nf-extsfns-idebugfailureanalysis2-getulong64.md) | The GetUlong64 method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it gets the ULONG64 value from the entry's data block. |
| [IDebugFailureAnalysis2::NextEntry](nf-extsfns-idebugfailureanalysis2-nextentry.md) | The NextEntry method gets the next FA entry, after a given FA entry, in a DebugFailureAnalysis object. |
| [IDebugFailureAnalysis2::SetBuffer](nf-extsfns-idebugfailureanalysis2-setbuffer.md) | The SetBuffer method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it overwrites the data block of the FA entry with the bytes in a specified buffer. |
| [IDebugFailureAnalysis2::SetExtensionCommand](nf-extsfns-idebugfailureanalysis2-setextensioncommand.md) | The SetExtensionCommand method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. |
| [IDebugFailureAnalysis2::SetString](nf-extsfns-idebugfailureanalysis2-setstring.md) | The SetString method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it sets (overwrites) the data block of the FA entry to a specified string value. |
| [IDebugFailureAnalysis2::SetUlong](nf-extsfns-idebugfailureanalysis2-setulong.md) | The SetUlong method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it sets (overwrites) the data block of the FA entry to a specified ULONG value. |
| [IDebugFailureAnalysis2::SetUlong64](nf-extsfns-idebugfailureanalysis2-setulong64.md) | The SetUlong64 method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it sets (overwrites) the data block of the FA entry to a specified ULONG64 value. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | extsfns.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff562112">!analyze</a>



<a href="https://msdn.microsoft.com/7648F789-85D5-4247-90DD-2EAA43543483">Writing an Analysis Extension Plug-in to Extend !analyze</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/jj983432">_EFN_Analyze</a>