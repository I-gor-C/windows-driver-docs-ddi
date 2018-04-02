---
UID: NS:ntddk._WHEA_PSHED_PLUGIN_CALLBACKS
title: "_WHEA_PSHED_PLUGIN_CALLBACKS"
author: windows-driver-content
description: The WHEA_PSHED_PLUGIN_CALLBACKS structure describes the callback functions for a PSHED plug-in.
old-location: whea\whea_pshed_plugin_callbacks.htm
old-project: whea
ms.assetid: 3b99f2bf-0ebc-40b2-a586-acc89200132b
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: "*PWHEA_PSHED_PLUGIN_CALLBACKS, PWHEA_PSHED_PLUGIN_CALLBACKS, PWHEA_PSHED_PLUGIN_CALLBACKS structure pointer [WHEA Drivers and Applications], WHEA_PSHED_PLUGIN_CALLBACKS, WHEA_PSHED_PLUGIN_CALLBACKS structure [WHEA Drivers and Applications], _WHEA_PSHED_PLUGIN_CALLBACKS, ntddk/PWHEA_PSHED_PLUGIN_CALLBACKS, ntddk/WHEA_PSHED_PLUGIN_CALLBACKS, whea.whea_pshed_plugin_callbacks, whearef_85037502-834f-412c-96e0-0a8d81cdd004.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddk.h
api_name:
-	WHEA_PSHED_PLUGIN_CALLBACKS
product: Windows
targetos: Windows
req.typenames: WHEA_PSHED_PLUGIN_CALLBACKS, *PWHEA_PSHED_PLUGIN_CALLBACKS
---

# _WHEA_PSHED_PLUGIN_CALLBACKS structure
The WHEA_PSHED_PLUGIN_CALLBACKS structure describes the callback functions for a PSHED plug-in.

## Syntax
```
typedef struct _WHEA_PSHED_PLUGIN_CALLBACKS {
  PSHED_PI_GET_ALL_ERROR_SOURCES      GetAllErrorSources;
  PVOID                               Reserved;
  PSHED_PI_GET_ERROR_SOURCE_INFO      GetErrorSourceInfo;
  PSHED_PI_SET_ERROR_SOURCE_INFO      SetErrorSourceInfo;
  PSHED_PI_ENABLE_ERROR_SOURCE        EnableErrorSource;
  PSHED_PI_DISABLE_ERROR_SOURCE       DisableErrorSource;
  PSHED_PI_WRITE_ERROR_RECORD         WriteErrorRecord;
  PSHED_PI_READ_ERROR_RECORD          ReadErrorRecord;
  PSHED_PI_CLEAR_ERROR_RECORD         ClearErrorRecord;
  PSHED_PI_RETRIEVE_ERROR_INFO        RetrieveErrorInfo;
  PSHED_PI_FINALIZE_ERROR_RECORD      FinalizeErrorRecord;
  PSHED_PI_CLEAR_ERROR_STATUS         ClearErrorStatus;
  PSHED_PI_ATTEMPT_ERROR_RECOVERY     AttemptRecovery;
  PSHED_PI_GET_INJECTION_CAPABILITIES GetInjectionCapabilities;
  PSHED_PI_INJECT_ERROR               InjectError;
} WHEA_PSHED_PLUGIN_CALLBACKS, *PWHEA_PSHED_PLUGIN_CALLBACKS;
```

## Members


`GetAllErrorSources`

A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/e9c97f88-aa13-4a3e-9236-c09703d17e4b">GetAllErrorSources</a> callback function. If a PSHED plug-in does not participate in error source discovery, this member should be set to <b>NULL</b>.

`Reserved`

Reserved for system use. This member should be set to <b>NULL</b>.

`GetErrorSourceInfo`

A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/8ede391a-acda-4540-a8bb-1b232695d632">GetErrorSourceInfo</a> callback function. If a PSHED plug-in does not participate in error source discovery, this member should be set to <b>NULL</b>.

`SetErrorSourceInfo`

A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/0b9cd546-d4ad-4e0e-92cb-7994c7327977">SetErrorSourceInfo</a> callback function. If a PSHED plug-in does not participate in error source control, this member should be set to <b>NULL</b>.

`EnableErrorSource`

A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/f2bc3b38-003e-4078-9bbd-d535e8971491">EnableErrorSource</a> callback function. If a PSHED plug-in does not participate in error source control, this member should be set to <b>NULL</b>.

`DisableErrorSource`

A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/062927db-9581-447a-820b-82687710ea8d">DisableErrorSource</a> callback function. If a PSHED plug-in does not participate in error source control, this member should be set to <b>NULL</b>.

`WriteErrorRecord`

A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/4800a0f9-29ee-4631-aee8-5a4924a08f55">WriteErrorRecord</a> callback function. If a PSHED plug-in does not participate in error record persistence, this member should be set to <b>NULL</b>.

`ReadErrorRecord`

A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/2fcbdfe3-bcce-4e5b-a16b-501612975e82">ReadErrorRecord</a> callback function. If a PSHED plug-in does not participate in error record persistence, this member should be set to <b>NULL</b>.

`ClearErrorRecord`

A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/e9893f9c-7fbd-4a02-8c2d-d7c480ed5198">ClearErrorRecord</a> callback function. If a PSHED plug-in does not participate in error record persistence, this member should be set to <b>NULL</b>.

`RetrieveErrorInfo`

A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/4d299057-a1cc-4b53-8ab4-031672181e74">RetrieveErrorInfo</a> callback function. If a PSHED plug-in does not participate in error information retrieval, this member should be set to <b>NULL</b>.

`FinalizeErrorRecord`

A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/68461243-ddf4-4883-84d2-4c105f1634b2">FinalizeErrorRecord</a> callback function. If a PSHED plug-in does not participate in error information retrieval, this member should be set to <b>NULL</b>.

`ClearErrorStatus`

A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/8b29edf3-be7f-4a8d-af96-2b1e985ba061">ClearErrorStatus</a> callback function. If a PSHED plug-in does not participate in error information retrieval, this member should be set to <b>NULL</b>.

`AttemptRecovery`

A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/e7186c16-f093-4a64-aa25-03e9ce0f967e">AttemptRecovery</a> callback function. If a PSHED plug-in does not participate in error recovery, this member should be set to <b>NULL</b>.

`GetInjectionCapabilities`

A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/8cb19677-11b8-4594-b4dd-ebd00fae07d4">GetInjectionCapabilities</a> callback function. If a PSHED plug-in does not participate in error injection, this member should be set to <b>NULL</b>.

`InjectError`

A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/efd2658b-875e-4589-9ba0-42232e070b91">InjectError</a> callback function. If a PSHED plug-in does not participate in error injection, this member should be set to <b>NULL</b>.

## Remarks
A WHEA_PSHED_PLUGIN_CALLBACKS structure is contained within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/e7186c16-f093-4a64-aa25-03e9ce0f967e">AttemptRecovery</a>



<a href="https://msdn.microsoft.com/e9893f9c-7fbd-4a02-8c2d-d7c480ed5198">ClearErrorRecord</a>



<a href="https://msdn.microsoft.com/8b29edf3-be7f-4a8d-af96-2b1e985ba061">ClearErrorStatus</a>



<a href="https://msdn.microsoft.com/062927db-9581-447a-820b-82687710ea8d">DisableErrorSource</a>



<a href="https://msdn.microsoft.com/f2bc3b38-003e-4078-9bbd-d535e8971491">EnableErrorSource</a>



<a href="https://msdn.microsoft.com/68461243-ddf4-4883-84d2-4c105f1634b2">FinalizeErrorRecord</a>



<a href="https://msdn.microsoft.com/e9c97f88-aa13-4a3e-9236-c09703d17e4b">GetAllErrorSources</a>



<a href="https://msdn.microsoft.com/8ede391a-acda-4540-a8bb-1b232695d632">GetErrorSourceInfo</a>



<a href="https://msdn.microsoft.com/8cb19677-11b8-4594-b4dd-ebd00fae07d4">GetInjectionCapabilities</a>



<a href="https://msdn.microsoft.com/efd2658b-875e-4589-9ba0-42232e070b91">InjectError</a>



<a href="https://msdn.microsoft.com/2fcbdfe3-bcce-4e5b-a16b-501612975e82">ReadErrorRecord</a>



<a href="https://msdn.microsoft.com/4d299057-a1cc-4b53-8ab4-031672181e74">RetrieveErrorInfo</a>



<a href="https://msdn.microsoft.com/0b9cd546-d4ad-4e0e-92cb-7994c7327977">SetErrorSourceInfo</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a>



<a href="https://msdn.microsoft.com/4800a0f9-29ee-4631-aee8-5a4924a08f55">WriteErrorRecord</a>