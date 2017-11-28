---
UID: NE.wdm._CLFS_MGMT_POLICY_TYPE
title: CLFS_MGMT_POLICY_TYPE
author: windows-driver-content
description: The CLFS_MGMT_POLICY_TYPE enumeration type identifies the type of a CLFS management policy.
old-location: kernel\clfs_mgmt_policy_type.htm
old-project: kernel
ms.assetid: 50e31ff1-07f2-4781-81f2-8db6e3cf9cc6
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CLFS_MGMT_POLICY_TYPE
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# CLFS_MGMT_POLICY_TYPE enumeration



## -description
<p>The <b>CLFS_MGMT_POLICY_TYPE</b> enumeration type identifies the type of a CLFS management policy.</p>


## -syntax

````
typedef enum _CLFS_MGMT_POLICY_TYPE { 
  ClfsMgmtPolicyMaximumSize            = 0,
  ClfsMgmtPolicyMinimumSize            = 1,
  ClfsMgmtPolicyNewContainerSize       = 2,
  ClfsMgmtPolicyGrowthRate             = 3,
  ClfsMgmtPolicyLogTail                = 4,
  ClfsMgmtPolicyAutoShrink             = 5,
  ClfsMgmtPolicyAutoGrow               = 6,
  ClfsMgmtPolicyNewContainerPrefix     = 7,
  ClfsMgmtPolicyNewContainerSuffix     = 8,
  ClfsMgmtPolicyNewContainerExtension  = 9,
  ClfsMgmtPolicyInvalid                = 10
} CLFS_MGMT_POLICY_TYPE, *PCLFS_MGMT_POLICY_TYPE;
````


## -enum-fields
<dl>

### -field <a id="ClfsMgmtPolicyMaximumSize"></a><a id="clfsmgmtpolicymaximumsize"></a><a id="CLFSMGMTPOLICYMAXIMUMSIZE"></a><b>ClfsMgmtPolicyMaximumSize</b>

<dd>
<p>Indicates a policy that specifies the maximum size of a log. </p>
</dd>

### -field <a id="ClfsMgmtPolicyMinimumSize"></a><a id="clfsmgmtpolicyminimumsize"></a><a id="CLFSMGMTPOLICYMINIMUMSIZE"></a><b>ClfsMgmtPolicyMinimumSize</b>

<dd>
<p>Indicates a policy that specifies the minimum size of a log. </p>
</dd>

### -field <a id="ClfsMgmtPolicyNewContainerSize"></a><a id="clfsmgmtpolicynewcontainersize"></a><a id="CLFSMGMTPOLICYNEWCONTAINERSIZE"></a><b>ClfsMgmtPolicyNewContainerSize</b>

<dd>
<p>Indicates a policy that specifies the size of new containers that are created.</p>
</dd>

### -field <a id="ClfsMgmtPolicyGrowthRate"></a><a id="clfsmgmtpolicygrowthrate"></a><a id="CLFSMGMTPOLICYGROWTHRATE"></a><b>ClfsMgmtPolicyGrowthRate</b>

<dd>
<p>Indicates a policy that specifies how many new containers will be added to the log each time the log grows.</p>
</dd>

### -field <a id="ClfsMgmtPolicyLogTail"></a><a id="clfsmgmtpolicylogtail"></a><a id="CLFSMGMTPOLICYLOGTAIL"></a><b>ClfsMgmtPolicyLogTail</b>

<dd>
<p>Indicates a policy that specifies how much free space will be requested when a client is notified to move its log tail. </p>
</dd>

### -field <a id="ClfsMgmtPolicyAutoShrink"></a><a id="clfsmgmtpolicyautoshrink"></a><a id="CLFSMGMTPOLICYAUTOSHRINK"></a><b>ClfsMgmtPolicyAutoShrink</b>

<dd>
<p>Indicates a policy that specifies when the log will shrink based on the percentage of the log that is free.</p>
</dd>

### -field <a id="ClfsMgmtPolicyAutoGrow"></a><a id="clfsmgmtpolicyautogrow"></a><a id="CLFSMGMTPOLICYAUTOGROW"></a><b>ClfsMgmtPolicyAutoGrow</b>

<dd>
<p>Indicates a policy that specifies whether the log should grow when fewer than two containers are free.</p>
</dd>

### -field <a id="ClfsMgmtPolicyNewContainerPrefix"></a><a id="clfsmgmtpolicynewcontainerprefix"></a><a id="CLFSMGMTPOLICYNEWCONTAINERPREFIX"></a><b>ClfsMgmtPolicyNewContainerPrefix</b>

<dd>
<p>Indicates a policy that specifies a prefix for the file name of each container, as well as the full path to the directory where the containers will be placed.</p>
</dd>

### -field <a id="ClfsMgmtPolicyNewContainerSuffix"></a><a id="clfsmgmtpolicynewcontainersuffix"></a><a id="CLFSMGMTPOLICYNEWCONTAINERSUFFIX"></a><b>ClfsMgmtPolicyNewContainerSuffix</b>

<dd>
<p>Indicates a policy that specifies a number to use as the starting suffix for container file names.</p>
</dd>

### -field <a id="ClfsMgmtPolicyNewContainerExtension"></a><a id="clfsmgmtpolicynewcontainerextension"></a><a id="CLFSMGMTPOLICYNEWCONTAINEREXTENSION"></a><b>ClfsMgmtPolicyNewContainerExtension</b>

<dd>
<p>Indicates a policy that specifies an extension for the file name of each container.</p>
</dd>

### -field <a id="ClfsMgmtPolicyInvalid"></a><a id="clfsmgmtpolicyinvalid"></a><a id="CLFSMGMTPOLICYINVALID"></a><b>ClfsMgmtPolicyInvalid</b>

<dd>
<p>Reserved for internal use.</p>
</dd>
</dl>

## -remarks
<p>Each type of CLFS management policy corresponds to a specific interpretation of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541842">CLFS_MGMT_POLICY</a> structure. The <b>PolicyType</b> member of the <b>CLFS_MGMT_POLICY</b> structure is a valid value of the <b>CLFS_MGMT_POLICY_TYPE</b> enumeration.</p>

<p>Each type of CLFS management policy corresponds to a specific interpretation of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541842">CLFS_MGMT_POLICY</a> structure. The <b>PolicyType</b> member of the <b>CLFS_MGMT_POLICY</b> structure is a valid value of the <b>CLFS_MGMT_POLICY_TYPE</b> enumeration.</p>

<p>Each type of CLFS management policy corresponds to a specific interpretation of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541842">CLFS_MGMT_POLICY</a> structure. The <b>PolicyType</b> member of the <b>CLFS_MGMT_POLICY</b> structure is a valid value of the <b>CLFS_MGMT_POLICY_TYPE</b> enumeration.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541842">CLFS_MGMT_POLICY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20CLFS_MGMT_POLICY_TYPE enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
