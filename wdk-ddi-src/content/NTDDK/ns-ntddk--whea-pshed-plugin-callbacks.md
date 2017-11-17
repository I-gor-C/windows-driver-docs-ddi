---
UID: NS.ntddk._WHEA_PSHED_PLUGIN_CALLBACKS
title: WHEA_PSHED_PLUGIN_CALLBACKS
author: windows-driver-content
description: The WHEA_PSHED_PLUGIN_CALLBACKS structure describes the callback functions for a PSHED plug-in.
old-location: whea\whea_pshed_plugin_callbacks.htm
ms.assetid: 3b99f2bf-0ebc-40b2-a586-acc89200132b
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: whea
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WHEA_PSHED_PLUGIN_CALLBACKS
req.alt-loc: ntddk.h
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
ms.keywords: WHEA_PSHED_PLUGIN_CALLBACKS, WHEA_PSHED_PLUGIN_CALLBACKS, *PWHEA_PSHED_PLUGIN_CALLBACKS
req.iface: 
---

# WHEA_PSHED_PLUGIN_CALLBACKS structure



## -description
<p>The WHEA_PSHED_PLUGIN_CALLBACKS structure describes the callback functions for a PSHED plug-in.</p>


## -syntax

````
typedef struct _WHEA_PSHED_PLUGIN_CALLBACKS {
  PSHED_PI_GET_ALL_ERROR_SOURCES      GetAllErrorSources;
  PVOID                               Reserved;
  PSHED_PI_GET_ERROR_SOURCE_INFO      GetErrorSourceInfo;
  PSHED_PI_SET_ERROR_SOURCE_INFO      SetErrorSourceInfo;
  PSHED_PI_ENABLE_ERROR_SOURCE        EnableErrorSource;
  PSHED_PI_DISABLE_ERROR_SOURCE       DisableErrorSource;
  PSHED_PI_WRITE_ERROR_RECORD         WriteErrorRecord;
  PSHED_PI_READ_ERROR_RECORD          ReadErrorRecord;
  PSHED_PI_CLEAR_ERROR_RECORD         ClearErrorRecord;
  PSHED_PI_RETRIEVE_ERROR_INFO        RetrieveErrorInfo;
  PSHED_PI_FINALIZE_ERROR_RECORD      FinalizeErrorRecord;
  PSHED_PI_CLEAR_ERROR_STATUS         ClearErrorStatus;
  PSHED_PI_ATTEMPT_ERROR_RECOVERY     AttemptRecovery;
  PSHED_PI_GET_INJECTION_CAPABILITIES GetInjectionCapabilities;
  PSHED_PI_INJECT_ERROR               InjectError;
} WHEA_PSHED_PLUGIN_CALLBACKS, *PWHEA_PSHED_PLUGIN_CALLBACKS;
````


## -struct-fields
<dl>

### -field <b>GetAllErrorSources</b>

<dd>
<p>A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/e9c97f88-aa13-4a3e-9236-c09703d17e4b">GetAllErrorSources</a> callback function. If a PSHED plug-in does not participate in error source discovery, this member should be set to <b>NULL</b>.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use. This member should be set to <b>NULL</b>.</p>
</dd>

### -field <b>GetErrorSourceInfo</b>

<dd>
<p>A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/8ede391a-acda-4540-a8bb-1b232695d632">GetErrorSourceInfo</a> callback function. If a PSHED plug-in does not participate in error source discovery, this member should be set to <b>NULL</b>.</p>
</dd>

### -field <b>SetErrorSourceInfo</b>

<dd>
<p>A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/0b9cd546-d4ad-4e0e-92cb-7994c7327977">SetErrorSourceInfo</a> callback function. If a PSHED plug-in does not participate in error source control, this member should be set to <b>NULL</b>.</p>
</dd>

### -field <b>EnableErrorSource</b>

<dd>
<p>A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/f2bc3b38-003e-4078-9bbd-d535e8971491">EnableErrorSource</a> callback function. If a PSHED plug-in does not participate in error source control, this member should be set to <b>NULL</b>.</p>
</dd>

### -field <b>DisableErrorSource</b>

<dd>
<p>A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/062927db-9581-447a-820b-82687710ea8d">DisableErrorSource</a> callback function. If a PSHED plug-in does not participate in error source control, this member should be set to <b>NULL</b>.</p>
</dd>

### -field <b>WriteErrorRecord</b>

<dd>
<p>A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/4800a0f9-29ee-4631-aee8-5a4924a08f55">WriteErrorRecord</a> callback function. If a PSHED plug-in does not participate in error record persistence, this member should be set to <b>NULL</b>.</p>
</dd>

### -field <b>ReadErrorRecord</b>

<dd>
<p>A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/2fcbdfe3-bcce-4e5b-a16b-501612975e82">ReadErrorRecord</a> callback function. If a PSHED plug-in does not participate in error record persistence, this member should be set to <b>NULL</b>.</p>
</dd>

### -field <b>ClearErrorRecord</b>

<dd>
<p>A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/e9893f9c-7fbd-4a02-8c2d-d7c480ed5198">ClearErrorRecord</a> callback function. If a PSHED plug-in does not participate in error record persistence, this member should be set to <b>NULL</b>.</p>
</dd>

### -field <b>RetrieveErrorInfo</b>

<dd>
<p>A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/4d299057-a1cc-4b53-8ab4-031672181e74">RetrieveErrorInfo</a> callback function. If a PSHED plug-in does not participate in error information retrieval, this member should be set to <b>NULL</b>.</p>
</dd>

### -field <b>FinalizeErrorRecord</b>

<dd>
<p>A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/68461243-ddf4-4883-84d2-4c105f1634b2">FinalizeErrorRecord</a> callback function. If a PSHED plug-in does not participate in error information retrieval, this member should be set to <b>NULL</b>.</p>
</dd>

### -field <b>ClearErrorStatus</b>

<dd>
<p>A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/8b29edf3-be7f-4a8d-af96-2b1e985ba061">ClearErrorStatus</a> callback function. If a PSHED plug-in does not participate in error information retrieval, this member should be set to <b>NULL</b>.</p>
</dd>

### -field <b>AttemptRecovery</b>

<dd>
<p>A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/e7186c16-f093-4a64-aa25-03e9ce0f967e">AttemptRecovery</a> callback function. If a PSHED plug-in does not participate in error recovery, this member should be set to <b>NULL</b>.</p>
</dd>

### -field <b>GetInjectionCapabilities</b>

<dd>
<p>A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/8cb19677-11b8-4594-b4dd-ebd00fae07d4">GetInjectionCapabilities</a> callback function. If a PSHED plug-in does not participate in error injection, this member should be set to <b>NULL</b>.</p>
</dd>

### -field <b>InjectError</b>

<dd>
<p>A pointer to the PSHED plug-in's <a href="https://msdn.microsoft.com/efd2658b-875e-4589-9ba0-42232e070b91">InjectError</a> callback function. If a PSHED plug-in does not participate in error injection, this member should be set to <b>NULL</b>.</p>
</dd>
</dl>

## -remarks
<p>A WHEA_PSHED_PLUGIN_CALLBACKS structure is contained within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/e7186c16-f093-4a64-aa25-03e9ce0f967e">AttemptRecovery</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/e9893f9c-7fbd-4a02-8c2d-d7c480ed5198">ClearErrorRecord</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8b29edf3-be7f-4a8d-af96-2b1e985ba061">ClearErrorStatus</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/062927db-9581-447a-820b-82687710ea8d">DisableErrorSource</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/f2bc3b38-003e-4078-9bbd-d535e8971491">EnableErrorSource</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/68461243-ddf4-4883-84d2-4c105f1634b2">FinalizeErrorRecord</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/e9c97f88-aa13-4a3e-9236-c09703d17e4b">GetAllErrorSources</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8ede391a-acda-4540-a8bb-1b232695d632">GetErrorSourceInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8cb19677-11b8-4594-b4dd-ebd00fae07d4">GetInjectionCapabilities</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/efd2658b-875e-4589-9ba0-42232e070b91">InjectError</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/2fcbdfe3-bcce-4e5b-a16b-501612975e82">ReadErrorRecord</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4d299057-a1cc-4b53-8ab4-031672181e74">RetrieveErrorInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/0b9cd546-d4ad-4e0e-92cb-7994c7327977">SetErrorSourceInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4800a0f9-29ee-4631-aee8-5a4924a08f55">WriteErrorRecord</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560617">WHEA_PSHED_PLUGIN_REGISTRATION_PACKET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_PSHED_PLUGIN_CALLBACKS structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
