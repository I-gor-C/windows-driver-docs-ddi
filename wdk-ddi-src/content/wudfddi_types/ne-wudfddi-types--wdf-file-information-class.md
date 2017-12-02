---
UID: NE.wudfddi_types._WDF_FILE_INFORMATION_CLASS
title: WDF_FILE_INFORMATION_CLASS
author: windows-driver-content
description: The WDF_FILE_INFORMATION_CLASS enumeration identifies the types of file information that a driver can obtain or set.
old-location: wdf\wdf_file_information_class.htm
old-project: wdf
ms.assetid: d9d6ce1b-8bc1-4ba7-8ee5-3172a780d52c
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WRITE_REGISTER_USHORT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wudfddi_types.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: WDF_FILE_INFORMATION_CLASS
req.alt-loc: Wudfddi_types.h,Wdffileobject.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# WDF_FILE_INFORMATION_CLASS enumeration



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>WDF_FILE_INFORMATION_CLASS</b> enumeration identifies the types of file information that a driver can obtain or set.</p>


## -syntax

````
typedef enum _WDF_FILE_INFORMATION_CLASS { 
  WdfFileInformationDirectory                 = 1,
  WdfFileInformationFullDirectory             = 2,
  WdfFileInformationBothDirectory             = 3,
  WdfFileInformationBasic                     = 4,
  WdfFileInformationStandard                  = 5,
  WdfFileInformationInternal                  = 6,
  WdfFileInformationEa                        = 7,
  WdfFileInformationAccess                    = 8,
  WdfFileInformationName                      = 9,
  WdfFileInformationRename                    = 10,
  WdfFileInformationLink                      = 11,
  WdfFileInformationNames                     = 12,
  WdfFileInformationDisposition               = 13,
  WdfFileInformationPosition                  = 14,
  WdfFileInformationFullEa                    = 15,
  WdfFileInformationMode                      = 16,
  WdfFileInformationAlignment                 = 17,
  WdfFileInformationAll                       = 18,
  WdfFileInformationAllocation                = 19,
  WdfFileInformationEndOfFile                 = 20,
  WdfFileInformationAlternateName             = 21,
  WdfFileInformationStream                    = 22,
  WdfFileInformationPipe                      = 23,
  WdfFileInformationPipeLocal                 = 24,
  WdfFileInformationPipeRemote                = 25,
  WdfFileInformationMailslotQuery             = 26,
  WdfFileInformationMailslotSet               = 27,
  WdfFileInformationCompression               = 28,
  WdfFileInformationObjectId                  = 29,
  WdfFileInformationCompletion                = 30,
  WdfFileInformationMoveCluster               = 31,
  WdfFileInformationQuota                     = 32,
  WdfFileInformationReparsePoint              = 33,
  WdfFileInformationNetworkOpen               = 34,
  WdfFileInformationAttributeTag              = 35,
  WdfFileInformationTracking                  = 36,
  WdfFileInformationIdBothDirectory           = 37,
  WdfFileInformationIdFullDirectory           = 38,
  WdfFileInformationValidDataLength           = 39,
  WdfFileInformationShortName                 = 40,
  WdfFileInformationIoCompletionNotification  = 41,
  WdfFileInformationIoStatusBlockRange        = 42,
  WdfFileInformationIoPriorityHint            = 43,
  WdfFileInformationSfioReserve               = 44,
  WdfFileInformationSfioVolume                = 45,
  WdfFileInformationHardLink                  = 46,
  WdfFileInformationProcessIdsUsingFile       = 47,
  WdfFileInformationNormalizedName            = 48,
  WdfFileInformationNetworkPhysicalName       = 49,
  WdfFileInformationIdGlobalTxDirectory       = 50,
  WdfFileInformationIsRemoteDevice            = 51,
  WdfFileInformationAttributeCache            = 52,
  WdfFileInformationMaximum                   = 53
} WDF_FILE_INFORMATION_CLASS, *PWDF_FILE_INFORMATION_CLASS;
````


## -enum-fields
<dl>

### -field WdfFileInformationDirectory

<dd></dd>

### -field WdfFileInformationFullDirectory

<dd></dd>

### -field WdfFileInformationBothDirectory

<dd></dd>

### -field WdfFileInformationBasic

<dd></dd>

### -field WdfFileInformationStandard

<dd></dd>

### -field WdfFileInformationInternal

<dd></dd>

### -field WdfFileInformationEa

<dd></dd>

### -field WdfFileInformationAccess

<dd></dd>

### -field WdfFileInformationName

<dd></dd>

### -field WdfFileInformationRename

<dd></dd>

### -field WdfFileInformationLink

<dd></dd>

### -field WdfFileInformationNames

<dd></dd>

### -field WdfFileInformationDisposition

<dd></dd>

### -field WdfFileInformationPosition

<dd></dd>

### -field WdfFileInformationFullEa

<dd></dd>

### -field WdfFileInformationMode

<dd></dd>

### -field WdfFileInformationAlignment

<dd></dd>

### -field WdfFileInformationAll

<dd></dd>

### -field WdfFileInformationAllocation

<dd></dd>

### -field WdfFileInformationEndOfFile

<dd></dd>

### -field WdfFileInformationAlternateName

<dd></dd>

### -field WdfFileInformationStream

<dd></dd>

### -field WdfFileInformationPipe

<dd></dd>

### -field WdfFileInformationPipeLocal

<dd></dd>

### -field WdfFileInformationPipeRemote

<dd></dd>

### -field WdfFileInformationMailslotQuery

<dd></dd>

### -field WdfFileInformationMailslotSet

<dd></dd>

### -field WdfFileInformationCompression

<dd></dd>

### -field WdfFileInformationObjectId

<dd></dd>

### -field WdfFileInformationCompletion

<dd></dd>

### -field WdfFileInformationMoveCluster

<dd></dd>

### -field WdfFileInformationQuota

<dd></dd>

### -field WdfFileInformationReparsePoint

<dd></dd>

### -field WdfFileInformationNetworkOpen

<dd></dd>

### -field WdfFileInformationAttributeTag

<dd></dd>

### -field WdfFileInformationTracking

<dd></dd>

### -field WdfFileInformationIdBothDirectory

<dd></dd>

### -field WdfFileInformationIdFullDirectory

<dd></dd>

### -field WdfFileInformationValidDataLength

<dd></dd>

### -field WdfFileInformationShortName

<dd></dd>

### -field WdfFileInformationIoCompletionNotification

<dd></dd>

### -field WdfFileInformationIoStatusBlockRange

<dd></dd>

### -field WdfFileInformationIoPriorityHint

<dd></dd>

### -field WdfFileInformationSfioReserve

<dd></dd>

### -field WdfFileInformationSfioVolume

<dd></dd>

### -field WdfFileInformationHardLink

<dd></dd>

### -field WdfFileInformationProcessIdsUsingFile

<dd></dd>

### -field WdfFileInformationNormalizedName

<dd></dd>

### -field WdfFileInformationNetworkPhysicalName

<dd></dd>

### -field WdfFileInformationIdGlobalTxDirectory

<dd></dd>

### -field WdfFileInformationIsRemoteDevice

<dd></dd>

### -field WdfFileInformationAttributeCache

<dd></dd>

### -field WdfFileInformationMaximum

<dd></dd>
</dl>

## -remarks
<p>The <b>WDF_FILE_INFORMATION_CLASS</b> enumeration is used as an input value to <a href="wdf.iwdfiorequest2_getqueryinformationparameters">IWDFIoRequest2::GetQueryInformationParameters</a> and as an output value from <a href="wdf.iwdfiorequest2_getsetinformationparameters">IWDFIoRequest2::GetSetInformationParameters</a>.</p>

<p>For most values that the <b>WDF_FILE_INFORMATION_CLASS</b> enumeration defines, the wdm.h or ntifs.h header file defines a FILE_XXXX_INFORMATION-named structure that the driver can use when obtaining or setting the file information.</p>

<p>For more information about the enumeration value and associated structures, see the description of the <i>FileInformationClass</i> parameter of <a href="..\wdm\nf-wdm-zwqueryinformationfile.md">ZwQueryInformationFile</a> and <a href="..\wdm\nf-wdm-zwsetinformationfile.md">ZwSetInformationFile</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.9</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi_types.h (include Wudfddi.h); </dt>
<dt>Wdffileobject.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.iwdfiorequest2_getqueryinformationparameters">IWDFIoRequest2::GetQueryInformationParameters</a>
</dt>
<dt>
<a href="wdf.iwdfiorequest2_getsetinformationparameters">IWDFIoRequest2::GetSetInformationParameters</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_FILE_INFORMATION_CLASS enumeration%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
