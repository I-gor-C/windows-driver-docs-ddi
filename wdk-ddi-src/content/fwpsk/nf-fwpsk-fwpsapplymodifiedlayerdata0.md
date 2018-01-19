---
UID : NF:fwpsk.FwpsApplyModifiedLayerData0
title : FwpsApplyModifiedLayerData0 function
author : windows-driver-content
description : The FwpsApplyModifiedLayerData0 function applies changes to layer-specific data made after a call to FwpsAcquireWritableLayerDataPointer0.Note  FwpsApplyModifiedLayerData0 is a specific version of FwpsApplyModifiedLayerData.
old-location : netvista\fwpsapplymodifiedlayerdata0.htm
old-project : netvista
ms.assetid : d32c19b6-462e-48e3-b22b-02542dca9cc4
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : FwpsApplyModifiedLayerData0
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : fwpsk.h
req.include-header : Fwpsk.h
req.target-type : Universal
req.target-min-winverclnt : Available starting with Windows 7.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : FwpsApplyModifiedLayerData0
req.alt-loc : fwpkclnt.lib,fwpkclnt.dll
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Fwpkclnt.lib
req.dll : 
req.irql : <= DISPATCH_LEVEL
req.typenames : FWPS_VSWITCH_EVENT_TYPE
---


# FwpsApplyModifiedLayerData0 function
The 
  <b>FwpsApplyModifiedLayerData0</b> function applies changes to layer-specific data made after a call to 
  <a href="..\fwpsk\nf-fwpsk-fwpsacquirewritablelayerdatapointer0.md">FwpsAcquireWritableLayerDataPointer0</a>.

## Syntax

````
void NTAPI FwpsApplyModifiedLayerData0(
  _In_ UINT64 classifyHandle,
  _In_ PVOID  modifiedLayerData,
  _In_ UINT32 flags
);
````

## Parameters

`classifyHandle`

The classification handle that identifies the callout driver's processing at the current layer.
     This handle is obtained by calling 
     <a href="..\fwpsk\nf-fwpsk-fwpsacquireclassifyhandle0.md">
     FwpsAcquireClassifyHandle0</a>.

`modifiedLayerData`

The data buffer obtained by calling 
     <a href="..\fwpsk\nf-fwpsk-fwpsacquirewritablelayerdatapointer0.md">FwpsAcquireWritableLayerDataPointer0</a> with members modified by the callout driver. Supported data
     types are defined as structures.

`flags`

The options to use with this function call. This flag can have the following
      value.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>


## Return Value

None.

## Remarks

<b>FwpsApplyModifiedLayerData0</b> should be called once for every call made to 
    <a href="..\fwpsk\nf-fwpsk-fwpsacquirewritablelayerdatapointer0.md">FwpsAcquireWritableLayerDataPointer0</a>, even if the callout driver didn't modify any data.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | fwpsk.h (include Fwpsk.h) |
| **Library** |  |
| **IRQL** | <= DISPATCH_LEVEL |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps_callout_classify_fn0.md">classifyFn</a>
</dt>
<dt>
<a href="..\fwpsk\ns-fwpsk-_fwps_bind_request0.md">FWPS_BIND_REQUEST0</a>
</dt>
<dt>
<a href="..\fwpsk\ns-fwpsk-_fwps_connect_request0.md">FWPS_CONNECT_REQUEST0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552389">FWPS_FILTER1</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsacquireclassifyhandle0.md">FwpsAcquireClassifyHandle0</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsacquirewritablelayerdatapointer0.md">
   FwpsAcquireWritableLayerDataPointer0</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsreleaseclassifyhandle0.md">FwpsReleaseClassifyHandle0</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsApplyModifiedLayerData0 function%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>