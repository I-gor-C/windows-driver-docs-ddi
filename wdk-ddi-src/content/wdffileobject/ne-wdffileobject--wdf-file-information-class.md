---
UID: NE.wdffileobject._WDF_FILE_INFORMATION_CLASS
title: WDF_FILE_INFORMATION_CLASS
author: windows-driver-content
description: The WDF_FILE_INFORMATION_CLASS enumeration identifies the types of file information that a driver can obtain or set.
old-location: wdf\wdf_file_information_class.htm
ms.assetid: d9d6ce1b-8bc1-4ba7-8ee5-3172a780d52c
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdffileobject.h
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
req.irql: <= DISPATCH_LEVEL
ms.keywords: WDF_FDO_EVENT_CALLBACKS, WDF_FDO_EVENT_CALLBACKS, *PWDF_FDO_EVENT_CALLBACKS
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

### -field <a id="WdfFileInformationDirectory"></a><a id="wdffileinformationdirectory"></a><a id="WDFFILEINFORMATIONDIRECTORY"></a><b>WdfFileInformationDirectory</b>

<dd></dd>

### -field <a id="WdfFileInformationFullDirectory"></a><a id="wdffileinformationfulldirectory"></a><a id="WDFFILEINFORMATIONFULLDIRECTORY"></a><b>WdfFileInformationFullDirectory</b>

<dd></dd>

### -field <a id="WdfFileInformationBothDirectory"></a><a id="wdffileinformationbothdirectory"></a><a id="WDFFILEINFORMATIONBOTHDIRECTORY"></a><b>WdfFileInformationBothDirectory</b>

<dd></dd>

### -field <a id="WdfFileInformationBasic"></a><a id="wdffileinformationbasic"></a><a id="WDFFILEINFORMATIONBASIC"></a><b>WdfFileInformationBasic</b>

<dd></dd>

### -field <a id="WdfFileInformationStandard"></a><a id="wdffileinformationstandard"></a><a id="WDFFILEINFORMATIONSTANDARD"></a><b>WdfFileInformationStandard</b>

<dd></dd>

### -field <a id="WdfFileInformationInternal"></a><a id="wdffileinformationinternal"></a><a id="WDFFILEINFORMATIONINTERNAL"></a><b>WdfFileInformationInternal</b>

<dd></dd>

### -field <a id="WdfFileInformationEa"></a><a id="wdffileinformationea"></a><a id="WDFFILEINFORMATIONEA"></a><b>WdfFileInformationEa</b>

<dd></dd>

### -field <a id="WdfFileInformationAccess"></a><a id="wdffileinformationaccess"></a><a id="WDFFILEINFORMATIONACCESS"></a><b>WdfFileInformationAccess</b>

<dd></dd>

### -field <a id="WdfFileInformationName"></a><a id="wdffileinformationname"></a><a id="WDFFILEINFORMATIONNAME"></a><b>WdfFileInformationName</b>

<dd></dd>

### -field <a id="WdfFileInformationRename"></a><a id="wdffileinformationrename"></a><a id="WDFFILEINFORMATIONRENAME"></a><b>WdfFileInformationRename</b>

<dd></dd>

### -field <a id="WdfFileInformationLink"></a><a id="wdffileinformationlink"></a><a id="WDFFILEINFORMATIONLINK"></a><b>WdfFileInformationLink</b>

<dd></dd>

### -field <a id="WdfFileInformationNames"></a><a id="wdffileinformationnames"></a><a id="WDFFILEINFORMATIONNAMES"></a><b>WdfFileInformationNames</b>

<dd></dd>

### -field <a id="WdfFileInformationDisposition"></a><a id="wdffileinformationdisposition"></a><a id="WDFFILEINFORMATIONDISPOSITION"></a><b>WdfFileInformationDisposition</b>

<dd></dd>

### -field <a id="WdfFileInformationPosition"></a><a id="wdffileinformationposition"></a><a id="WDFFILEINFORMATIONPOSITION"></a><b>WdfFileInformationPosition</b>

<dd></dd>

### -field <a id="WdfFileInformationFullEa"></a><a id="wdffileinformationfullea"></a><a id="WDFFILEINFORMATIONFULLEA"></a><b>WdfFileInformationFullEa</b>

<dd></dd>

### -field <a id="WdfFileInformationMode"></a><a id="wdffileinformationmode"></a><a id="WDFFILEINFORMATIONMODE"></a><b>WdfFileInformationMode</b>

<dd></dd>

### -field <a id="WdfFileInformationAlignment"></a><a id="wdffileinformationalignment"></a><a id="WDFFILEINFORMATIONALIGNMENT"></a><b>WdfFileInformationAlignment</b>

<dd></dd>

### -field <a id="WdfFileInformationAll"></a><a id="wdffileinformationall"></a><a id="WDFFILEINFORMATIONALL"></a><b>WdfFileInformationAll</b>

<dd></dd>

### -field <a id="WdfFileInformationAllocation"></a><a id="wdffileinformationallocation"></a><a id="WDFFILEINFORMATIONALLOCATION"></a><b>WdfFileInformationAllocation</b>

<dd></dd>

### -field <a id="WdfFileInformationEndOfFile"></a><a id="wdffileinformationendoffile"></a><a id="WDFFILEINFORMATIONENDOFFILE"></a><b>WdfFileInformationEndOfFile</b>

<dd></dd>

### -field <a id="WdfFileInformationAlternateName"></a><a id="wdffileinformationalternatename"></a><a id="WDFFILEINFORMATIONALTERNATENAME"></a><b>WdfFileInformationAlternateName</b>

<dd></dd>

### -field <a id="WdfFileInformationStream"></a><a id="wdffileinformationstream"></a><a id="WDFFILEINFORMATIONSTREAM"></a><b>WdfFileInformationStream</b>

<dd></dd>

### -field <a id="WdfFileInformationPipe"></a><a id="wdffileinformationpipe"></a><a id="WDFFILEINFORMATIONPIPE"></a><b>WdfFileInformationPipe</b>

<dd></dd>

### -field <a id="WdfFileInformationPipeLocal"></a><a id="wdffileinformationpipelocal"></a><a id="WDFFILEINFORMATIONPIPELOCAL"></a><b>WdfFileInformationPipeLocal</b>

<dd></dd>

### -field <a id="WdfFileInformationPipeRemote"></a><a id="wdffileinformationpiperemote"></a><a id="WDFFILEINFORMATIONPIPEREMOTE"></a><b>WdfFileInformationPipeRemote</b>

<dd></dd>

### -field <a id="WdfFileInformationMailslotQuery"></a><a id="wdffileinformationmailslotquery"></a><a id="WDFFILEINFORMATIONMAILSLOTQUERY"></a><b>WdfFileInformationMailslotQuery</b>

<dd></dd>

### -field <a id="WdfFileInformationMailslotSet"></a><a id="wdffileinformationmailslotset"></a><a id="WDFFILEINFORMATIONMAILSLOTSET"></a><b>WdfFileInformationMailslotSet</b>

<dd></dd>

### -field <a id="WdfFileInformationCompression"></a><a id="wdffileinformationcompression"></a><a id="WDFFILEINFORMATIONCOMPRESSION"></a><b>WdfFileInformationCompression</b>

<dd></dd>

### -field <a id="WdfFileInformationObjectId"></a><a id="wdffileinformationobjectid"></a><a id="WDFFILEINFORMATIONOBJECTID"></a><b>WdfFileInformationObjectId</b>

<dd></dd>

### -field <a id="WdfFileInformationCompletion"></a><a id="wdffileinformationcompletion"></a><a id="WDFFILEINFORMATIONCOMPLETION"></a><b>WdfFileInformationCompletion</b>

<dd></dd>

### -field <a id="WdfFileInformationMoveCluster"></a><a id="wdffileinformationmovecluster"></a><a id="WDFFILEINFORMATIONMOVECLUSTER"></a><b>WdfFileInformationMoveCluster</b>

<dd></dd>

### -field <a id="WdfFileInformationQuota"></a><a id="wdffileinformationquota"></a><a id="WDFFILEINFORMATIONQUOTA"></a><b>WdfFileInformationQuota</b>

<dd></dd>

### -field <a id="WdfFileInformationReparsePoint"></a><a id="wdffileinformationreparsepoint"></a><a id="WDFFILEINFORMATIONREPARSEPOINT"></a><b>WdfFileInformationReparsePoint</b>

<dd></dd>

### -field <a id="WdfFileInformationNetworkOpen"></a><a id="wdffileinformationnetworkopen"></a><a id="WDFFILEINFORMATIONNETWORKOPEN"></a><b>WdfFileInformationNetworkOpen</b>

<dd></dd>

### -field <a id="WdfFileInformationAttributeTag"></a><a id="wdffileinformationattributetag"></a><a id="WDFFILEINFORMATIONATTRIBUTETAG"></a><b>WdfFileInformationAttributeTag</b>

<dd></dd>

### -field <a id="WdfFileInformationTracking"></a><a id="wdffileinformationtracking"></a><a id="WDFFILEINFORMATIONTRACKING"></a><b>WdfFileInformationTracking</b>

<dd></dd>

### -field <a id="WdfFileInformationIdBothDirectory"></a><a id="wdffileinformationidbothdirectory"></a><a id="WDFFILEINFORMATIONIDBOTHDIRECTORY"></a><b>WdfFileInformationIdBothDirectory</b>

<dd></dd>

### -field <a id="WdfFileInformationIdFullDirectory"></a><a id="wdffileinformationidfulldirectory"></a><a id="WDFFILEINFORMATIONIDFULLDIRECTORY"></a><b>WdfFileInformationIdFullDirectory</b>

<dd></dd>

### -field <a id="WdfFileInformationValidDataLength"></a><a id="wdffileinformationvaliddatalength"></a><a id="WDFFILEINFORMATIONVALIDDATALENGTH"></a><b>WdfFileInformationValidDataLength</b>

<dd></dd>

### -field <a id="WdfFileInformationShortName"></a><a id="wdffileinformationshortname"></a><a id="WDFFILEINFORMATIONSHORTNAME"></a><b>WdfFileInformationShortName</b>

<dd></dd>

### -field <a id="WdfFileInformationIoCompletionNotification"></a><a id="wdffileinformationiocompletionnotification"></a><a id="WDFFILEINFORMATIONIOCOMPLETIONNOTIFICATION"></a><b>WdfFileInformationIoCompletionNotification</b>

<dd></dd>

### -field <a id="WdfFileInformationIoStatusBlockRange"></a><a id="wdffileinformationiostatusblockrange"></a><a id="WDFFILEINFORMATIONIOSTATUSBLOCKRANGE"></a><b>WdfFileInformationIoStatusBlockRange</b>

<dd></dd>

### -field <a id="WdfFileInformationIoPriorityHint"></a><a id="wdffileinformationiopriorityhint"></a><a id="WDFFILEINFORMATIONIOPRIORITYHINT"></a><b>WdfFileInformationIoPriorityHint</b>

<dd></dd>

### -field <a id="WdfFileInformationSfioReserve"></a><a id="wdffileinformationsfioreserve"></a><a id="WDFFILEINFORMATIONSFIORESERVE"></a><b>WdfFileInformationSfioReserve</b>

<dd></dd>

### -field <a id="WdfFileInformationSfioVolume"></a><a id="wdffileinformationsfiovolume"></a><a id="WDFFILEINFORMATIONSFIOVOLUME"></a><b>WdfFileInformationSfioVolume</b>

<dd></dd>

### -field <a id="WdfFileInformationHardLink"></a><a id="wdffileinformationhardlink"></a><a id="WDFFILEINFORMATIONHARDLINK"></a><b>WdfFileInformationHardLink</b>

<dd></dd>

### -field <a id="WdfFileInformationProcessIdsUsingFile"></a><a id="wdffileinformationprocessidsusingfile"></a><a id="WDFFILEINFORMATIONPROCESSIDSUSINGFILE"></a><b>WdfFileInformationProcessIdsUsingFile</b>

<dd></dd>

### -field <a id="WdfFileInformationNormalizedName"></a><a id="wdffileinformationnormalizedname"></a><a id="WDFFILEINFORMATIONNORMALIZEDNAME"></a><b>WdfFileInformationNormalizedName</b>

<dd></dd>

### -field <a id="WdfFileInformationNetworkPhysicalName"></a><a id="wdffileinformationnetworkphysicalname"></a><a id="WDFFILEINFORMATIONNETWORKPHYSICALNAME"></a><b>WdfFileInformationNetworkPhysicalName</b>

<dd></dd>

### -field <a id="WdfFileInformationIdGlobalTxDirectory"></a><a id="wdffileinformationidglobaltxdirectory"></a><a id="WDFFILEINFORMATIONIDGLOBALTXDIRECTORY"></a><b>WdfFileInformationIdGlobalTxDirectory</b>

<dd></dd>

### -field <a id="WdfFileInformationIsRemoteDevice"></a><a id="wdffileinformationisremotedevice"></a><a id="WDFFILEINFORMATIONISREMOTEDEVICE"></a><b>WdfFileInformationIsRemoteDevice</b>

<dd></dd>

### -field <a id="WdfFileInformationAttributeCache"></a><a id="wdffileinformationattributecache"></a><a id="WDFFILEINFORMATIONATTRIBUTECACHE"></a><b>WdfFileInformationAttributeCache</b>

<dd></dd>

### -field <a id="WdfFileInformationMaximum"></a><a id="wdffileinformationmaximum"></a><a id="WDFFILEINFORMATIONMAXIMUM"></a><b>WdfFileInformationMaximum</b>

<dd></dd>
</dl>

## -remarks
<p>The <b>WDF_FILE_INFORMATION_CLASS</b> enumeration is used as an input value to <a href="https://msdn.microsoft.com/library/windows/hardware/ff558997">IWDFIoRequest2::GetQueryInformationParameters</a> and as an output value from <a href="https://msdn.microsoft.com/library/windows/hardware/ff559009">IWDFIoRequest2::GetSetInformationParameters</a>.</p>

<p>For most values that the <b>WDF_FILE_INFORMATION_CLASS</b> enumeration defines, the wdm.h or ntifs.h header file defines a FILE_XXXX_INFORMATION-named structure that the driver can use when obtaining or setting the file information.</p>

<p>For more information about the enumeration value and associated structures, see the description of the <i>FileInformationClass</i> parameter of <a href="https://msdn.microsoft.com/library/windows/hardware/ff567052">ZwQueryInformationFile</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a>.</p>

<p>The <b>WDF_FILE_INFORMATION_CLASS</b> enumeration is used as an input value to <a href="https://msdn.microsoft.com/library/windows/hardware/ff558997">IWDFIoRequest2::GetQueryInformationParameters</a> and as an output value from <a href="https://msdn.microsoft.com/library/windows/hardware/ff559009">IWDFIoRequest2::GetSetInformationParameters</a>.</p>

<p>For most values that the <b>WDF_FILE_INFORMATION_CLASS</b> enumeration defines, the wdm.h or ntifs.h header file defines a FILE_XXXX_INFORMATION-named structure that the driver can use when obtaining or setting the file information.</p>

<p>For more information about the enumeration value and associated structures, see the description of the <i>FileInformationClass</i> parameter of <a href="https://msdn.microsoft.com/library/windows/hardware/ff567052">ZwQueryInformationFile</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a>.</p>

<p>The <b>WDF_FILE_INFORMATION_CLASS</b> enumeration is used as an input value to <a href="https://msdn.microsoft.com/library/windows/hardware/ff558997">IWDFIoRequest2::GetQueryInformationParameters</a> and as an output value from <a href="https://msdn.microsoft.com/library/windows/hardware/ff559009">IWDFIoRequest2::GetSetInformationParameters</a>.</p>

<p>For most values that the <b>WDF_FILE_INFORMATION_CLASS</b> enumeration defines, the wdm.h or ntifs.h header file defines a FILE_XXXX_INFORMATION-named structure that the driver can use when obtaining or setting the file information.</p>

<p>For more information about the enumeration value and associated structures, see the description of the <i>FileInformationClass</i> parameter of <a href="https://msdn.microsoft.com/library/windows/hardware/ff567052">ZwQueryInformationFile</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567096">ZwSetInformationFile</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558997">IWDFIoRequest2::GetQueryInformationParameters</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559009">IWDFIoRequest2::GetSetInformationParameters</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_FILE_INFORMATION_CLASS enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
